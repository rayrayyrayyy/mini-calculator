# Ray Allessandra D. Pacis | BSCPE 1-5

# import tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# define a function for addition of numbers
def addition():
    try:
        result = float(first_num.get()) + float(second_num.get()) # variable first_num and second_num to be follow
    except:
        messagebox.showerror("Showerror", "ERROR! Invalid input!\n Please enter numbers only.")
    
# define a function for subtraction of numbers
# define a function for multiplication of numbers
# define a function for division of numbers

# open a window using tkinter
root_window = Tk()
root_window.title("MINI CALCULATOR")
root_window.geometry("500x500")

# create buttons
# define a function to open another window based on the button that the user clicked
# create entry 
# create exit button

# mainloop
root_window.mainloop()