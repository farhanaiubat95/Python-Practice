import torch
import torch.nn as nn
import torchvision.models as models
from einops.layers.torch import Rearrange
from torchvision.models.resnet import ResNet50_Weights

class TransformerBlock(nn.Module):
    def __init__(self, dim, heads=8, mlp_dim=2048):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim=dim, num_heads=heads, batch_first=True)
        self.norm1 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, mlp_dim),
            nn.GELU(),
            nn.Linear(mlp_dim, dim)
        )
        self.norm2 = nn.LayerNorm(dim)

    def forward(self, x):
        attn_output, _ = self.attn(x, x, x)
        x = self.norm1(x + attn_output)
        x = self.norm2(x + self.mlp(x))
        return x

class ResFormer(nn.Module):
    def __init__(self, num_classes=3):
        super().__init__()
        resnet = models.resnet50(weights=ResNet50_Weights.DEFAULT)
        self.backbone = nn.Sequential(*list(resnet.children())[:-2])  # Remove last FC layer
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.flatten = nn.Flatten()

        self.tokenizer = nn.Sequential(
            nn.Conv2d(2048, 512, kernel_size=1),
            Rearrange('b c h w -> b (h w) c')  # Flatten spatial dimensions
        )

        self.transformer = TransformerBlock(dim=512)
        self.head = nn.Sequential(
            nn.LayerNorm(512),
            nn.Linear(512, num_classes)
        )

    def forward(self, x):
        x = self.backbone(x)               # [B, 2048, 7, 7]
        x = self.tokenizer(x)              # [B, 49, 512]
        x = self.transformer(x)            # [B, 49, 512]
        x = x.mean(dim=1)                  # Global average pooling over tokens
        return self.head(x)                # [B, num_classes]
