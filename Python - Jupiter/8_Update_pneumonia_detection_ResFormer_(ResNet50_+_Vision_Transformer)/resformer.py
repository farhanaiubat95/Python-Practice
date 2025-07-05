# resformer.py
import torch
import torch.nn as nn
import torchvision.models as models
from einops.layers.torch import Rearrange
from torchvision.models.resnet import ResNet50_Weights

class PositionalEncoding(nn.Module):
    def __init__(self, dim, max_len=49):
        super().__init__()
        pe = torch.zeros(max_len, dim)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, dim, 2).float() * (-torch.log(torch.tensor(10000.0)) / dim))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]

class TransformerBlock(nn.Module):
    def __init__(self, dim, heads=8, mlp_dim=2048, dropout=0.1):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim=dim, num_heads=heads, batch_first=True, dropout=dropout)
        self.norm1 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, mlp_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(mlp_dim, dim)
        )
        self.norm2 = nn.LayerNorm(dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        attn_output, _ = self.attn(x, x, x)
        x = self.norm1(x + self.dropout(attn_output))
        x = self.norm2(x + self.dropout(self.mlp(x)))
        return x

class ResFormer(nn.Module):
    def __init__(self, num_classes=3, num_transformers=2):
        super().__init__()
        resnet = models.resnet50(weights=ResNet50_Weights.DEFAULT)
        self.backbone = nn.Sequential(*list(resnet.children())[:-2])
        self.tokenizer = nn.Sequential(
            nn.Conv2d(2048, 512, kernel_size=1),
            Rearrange('b c h w -> b (h w) c')
        )
        self.pos_encoder = PositionalEncoding(dim=512)

        self.transformer_layers = nn.Sequential(*[
            TransformerBlock(dim=512) for _ in range(num_transformers)
        ])

        self.head = nn.Sequential(
            nn.LayerNorm(512),
            nn.Linear(512, num_classes)
        )

    def forward(self, x):
        x = self.backbone(x)
        x = self.tokenizer(x)
        x = self.pos_encoder(x)
        x = self.transformer_layers(x)
        x = x.mean(dim=1)
        return self.head(x)
