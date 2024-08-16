# tkinter
import math
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


calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evalute_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def back(self):
    self.line.backspace()


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# for graphical interface
root = tk.Tk()
root.geometry("422x350")
root.resizable(width=False, height=False)  # can't change the calculator size
# configure
root.configure(background="gray", padx=2, pady=2)

# text area
root.title("Python Calculator")
label = tk.Label(root, text="Fx Calculator", bg="gray", fg="white", justify="center", font=("Arial", 10, "bold")).grid(
    row=0, sticky='n'+'s'+'e'+'w', column=0, ipady=5)

text_result = tk.Text(root, height=1, width=26,
                      bg="gainsboro", fg="navy", bd=10, font=("Arial", 20, "bold"))

text_result.grid(sticky='n'+'s'+'e'+'w', columnspan=6, ipady=10)


# button - sticky='n'+'s'+'e'+'w'
# Button row - 1
btn_del = tk.Button(root, text="DEL", command=clear_field, height=1, width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="darkgoldenrod2",
                    activebackground="cadetblue", cursor="hand2", bg="darkgoldenrod2", fg="black")
btn_del.grid(row=2, sticky='n'+'s'+'e'+'w', column=0)

btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation(
    "."), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_dot.grid(row=2, sticky='n'+'s'+'e'+'w', column=1, columnspan=2)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(
    7), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_7.grid(row=2, sticky='w'+'e', column=3)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(
    8), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_8.grid(row=2, sticky='n'+'s'+'e'+'w', column=4)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(
    9), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_9.grid(row=2, sticky='n'+'s'+'e'+'w', column=5)


# Button row - 2
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), height=1, width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="darkgoldenrod2",
                     activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_plus.grid(row=3, sticky='n'+'s'+'e'+'w', column=0)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="darkgoldenrod2",
                      activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_minus.grid(row=3, sticky='n'+'s'+'e'+'w', column=1)

btn_open_brac = tk.Button(root, text="(", command=lambda: add_to_calculation(
    "("), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_open_brac.grid(row=3, sticky='n'+'s'+'e'+'w', column=2)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(
    4), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_4.grid(row=3, sticky='w'+'e', column=3)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(
    5), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_5.grid(row=3, sticky='n'+'s'+'e'+'w', column=4)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(
    6), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_6.grid(row=3, sticky='n'+'s'+'e'+'w', column=5)


# Button row - 2
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), height=1, width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="darkgoldenrod2",
                    activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_div.grid(row=4, sticky='n'+'s'+'e'+'w', column=0)

btn_mul = tk.Button(root, text="X", command=lambda: add_to_calculation("*"), width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="darkgoldenrod2",
                    activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_mul.grid(row=4, sticky='n'+'s'+'e'+'w', column=1)

btn_close_brac = tk.Button(root, text=")", command=lambda: add_to_calculation(
    ")"), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_close_brac.grid(row=4, sticky='n'+'s'+'e'+'w', column=2)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(
    1), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_1.grid(row=4, sticky='w'+'e', column=3)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(
    2), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_2.grid(row=4, sticky='n'+'s'+'e'+'w', column=4)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(
    3), width=3, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
    activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_3.grid(row=4, sticky='n'+'s'+'e'+'w', column=5)


# Button row - 3
btn_Ans = tk.Button(root, text="Ans", command=evalute_calculation, height=1, width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="darkgoldenrod2",
                    activebackground="cadetblue", cursor="hand2", bg="cyan3", fg="black")
btn_Ans.grid(row=5, sticky='n'+'s'+'e'+'w', column=0, columnspan=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=4, font=("Arial", 14, "bold"), bd=6, activeforeground="black",
                  activebackground="cadetblue", cursor="hand2", bg="black", fg="aqua")
btn_0.grid(row=5, sticky='n'+'s'+'e'+'w', column=3, columnspan=3)


root.mainloop()
