# Ray Allessandra D. Pacis | BSCPE 1-5

# import tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# define a function for addition of numbers
def addition():
    # create another window
    value_window = Tk()
    value_window.title("MINI CALCULATOR")
    value_window.geometry("500x300")
    value_window.config(bg = "cyan")

    # set variables for first number
    first_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    first_num.place(x=200, y=10)

    # add label for first number
    note = Label(value_window, text = "Enter first number:", font=("Times", 15), justify = CENTER)
    note.place(x=10, y=10)

    # set variables for second number
    second_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    second_num.place(x=200, y=40)

    # add label for second number
    note1 = Label(value_window, text = "Enter second number:", font=("Times", 15), justify = CENTER)
    note1.place(x=10, y=40)

    result = Label(value_window, text = "", font=("Times", 15), justify = CENTER)
    result.place(x=200, y=80)
    try:
        total = float(first_num.get()) + float(second_num.get()) 
        result.config(text = total)

    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")
    
# define a function for subtraction of numbers
def subtract():
    try:
        total = float(first_num.get()) - float(second_num.get()) 
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")

# define a function for multiplication of numbers
def multiply():
    try:
        total = float(first_num.get()) * float(second_num.get()) 
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")

# define a function for division of numbers
def divide():
    try:
        total = float(first_num.get()) / float(second_num.get()) 
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")

# open a window using tkinter
root_window = Tk()
root_window.title("MINI CALCULATOR")
root_window.geometry("385x300")
root_window.config(bg = "brown")

# create buttons
# addition button
add_button = Button(root_window, text = "ADDITION", width = 20, command = addition)
add_button.place(x=30, y=20)
# subtraction button
subtract_button = Button(root_window, text = "SUBTRACTION", width = 20)
subtract_button.place(x=200, y=20)
# multiplication button
multiply_button = Button(root_window, text = "MULTIPLICATION", width = 20)
multiply_button.place(x=30, y=60)
# division button
division_button = Button(root_window, text = "DIVISION", width = 20)
division_button.place(x=200, y=60)

# mainloop
root_window.mainloop()