# tkinter
import tkinter as tk

# Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = tk.Tk()
root.geometry("500x250")
root.title("TCWF")

# # Lebel
# # w=Label(master, option=value)
# # master is the parameter used to represent the parent window.
text_var = tk.StringVar()
text_var.set("Tkinter Lerning")
w = tk.Label(root,
             #  text='Tkinter Lerning'
             textvariable=text_var,
             anchor="center",
             bg="green",
             fg="red",
             height=2,
             width=40,
             bd=3,
             padx=2,
             pady=2,
             cursor="hand1",
             justify=tk.LEFT,
             relief=tk.RAISED,  # border design
             font=("Arial", 10, "bold"),
             underline=3,  # index number
             wraplength=250
             ).grid(row=0, column=0)


# Button
# w=Button(master, option=value)
# flash():
# invoke():

def button_clicked():
    print("Button clicked!")


button = tk.Button(root,
                   text="Click Me",
                   command=button_clicked,
                   bd=3,
                   height=2,
                   width=15,
                   padx=0,
                   pady=0,
                   activebackground="blue",
                   activeforeground="white",
                   bg="lightgray",
                   fg="black",
                   disabledforeground="gray",
                   anchor="center",
                   cursor="hand2",
                   font=("Arial", 12),
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   wraplength=100
                   ).grid(row=1, column=0)


# Entry
# It is used to input the single line text entry from the user
# w=Entry(master, option=value)
tk.Label(root, text='First Name : ', width=10).grid(row=2, column=0)
e1 = tk.Entry(root, width=50)
e1.grid(row=2, column=1)


"""
mainloop() is used when your application is ready to run. 
mainloop() is an infinite loop used to run the application, 
wait for an event to occur, and process the event as long as the window is not closed.
"""
root.mainloop()
