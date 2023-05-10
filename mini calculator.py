# Ray Allessandra D. Pacis | BSCPE 1-5

# import tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# define a function for addition of numbers
def addition():
    try:
        total = float(first_num.get()) + float(second_num.get()) # variable first_num and second_num to be follow
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")
    
# define a function for subtraction of numbers
def subtract():
    try:
        total = float(first_num.get()) - float(second_num.get()) # variable first_num and second_num to be follow
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")

# define a function for multiplication of numbers
def multiply():
    try:
        total = float(first_num.get()) * float(second_num.get()) # variable first_num and second_num to be follow
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")

# define a function for division of numbers
def divide():
    try:
        total = float(first_num.get()) / float(second_num.get()) # variable first_num and second_num to be follow
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")

# open a window using tkinter
root_window = Tk()
root_window.title("MINI CALCULATOR")
root_window.geometry("385x300")
root_window.config(bg = "brown")

# set variables for first and second number
first_num = Entry(root_window, font=("Segoe Script",20), justify = CENTER)
second_num = Entry(root_window, font=("Segoe Script",20), justify = CENTER)

# create buttons
add_button = Button(root_window, text = "ADDITION", width = 20)
add_button.place(x=30, y=20)

subtract_button = Button(root_window, text = "SUBTRACTION", width = 20)
subtract_button.place(x=200, y=20)

multiply_button = Button(root_window, text = "MULTIPLICATION", width = 20)
multiply_button.place(x=30, y=60)

division_button = Button(root_window, text = "DIVISION", width = 20)
division_button.place(x=200, y=60)


# define a function to open another window based on the button that the user clicked
# create entry 
# create exit button

# mainloop
root_window.mainloop()