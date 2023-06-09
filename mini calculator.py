# Ray Allessandra D. Pacis | BSCPE 1-5

# import tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# define a function for addition of numbers
def addition():
    # create another window for addition
    value_window = Toplevel(root_window)
    value_window.title("ADDITION")
    value_window.geometry("430x260")
    value_window.config(bg = "cyan")

    # set variables for first number
    first_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    first_num.place(x=200, y=10)

    # add label for first number
    note = Label(value_window, text = "Enter first number:", bg = "cyan", font=("Times", 15), justify = CENTER)
    note.place(x=10, y=10)

    # set variables for second number
    second_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    second_num.place(x=200, y=40)

    # add label for second number
    note1 = Label(value_window, text = "Enter second number:", bg = "cyan", font=("Times", 15), justify = CENTER)
    note1.place(x=10, y=40)

    # add label for result
    result = Label(value_window, text = "Result\t= ", bg = "cyan", font=("Times", 20), justify = CENTER)
    result.place(x=50, y=130)

    # add back button
    back_button = Button(value_window, text = "BACK", width = 20, command = value_window.destroy)
    back_button.place(x=225, y=200)

    # define clear
    def clear():
        first_num.delete(0, END)
        second_num.delete(0, END)

    # add clear button
    clear_button = Button(value_window, text = "CLEAR", width = 20, command = clear)
    clear_button.place(x=50, y=200)

    def add():
        try:
            total = float(first_num.get()) + float(second_num.get())
            entry.config(text = total)
        except:
            messagebox.showerror("ERROR", "ERROR! Invalid input!\n Please enter numbers only.")
    # entry
    entry = Label(value_window, text = "", bg = "cyan", font=("Times", 20), justify = CENTER)
    entry.place(x=200, y=130)

    # result button
    result_button = Button(value_window, text = "SHOW RESULT", width = 20, command = add)
    result_button.place(x=225, y=80)   

# define a function for subtraction of numbers
def subtract():
    # create another window for subtraction
    value_window = Toplevel(root_window)
    value_window.title("SUBTRACTION")
    value_window.geometry("430x260")
    value_window.config(bg = "green")

    # set variables for first number
    first_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    first_num.place(x=200, y=10)

    # add label for first number
    note = Label(value_window, text = "Enter first number:", bg = "green", font=("Times", 15), justify = CENTER)
    note.place(x=10, y=10)

    # set variables for second number
    second_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    second_num.place(x=200, y=40)

    # add label for second number
    note1 = Label(value_window, text = "Enter second number:", bg = "green", font=("Times", 15), justify = CENTER)
    note1.place(x=10, y=40)

    # add label for result
    result = Label(value_window, text = "Result\t= ", bg = "green", font=("Times", 20), justify = CENTER)
    result.place(x=50, y=130)

    # add back button
    back_button = Button(value_window, text = "BACK", width = 20, command = value_window.destroy)
    back_button.place(x=225, y=200)

    # define clear
    def clear():
        first_num.delete(0, END)
        second_num.delete(0, END)

    # add clear button
    clear_button = Button(value_window, text = "CLEAR", width = 20, command = clear)
    clear_button.place(x=50, y=200)

    def sub():
        try:
            total = float(first_num.get()) - float(second_num.get()) 
            entry.config(text = total)
        except:
            messagebox.showerror("ERROR", "ERROR! Invalid input!\n Please enter numbers only.")
    # entry
    entry = Label(value_window, text = "", bg = "green", font=("Times", 20), justify = CENTER)
    entry.place(x=200, y=130)

    # result button
    result_button = Button(value_window, text = "SHOW RESULT", width = 20, command = sub)
    result_button.place(x=225, y=80)

# define a function for multiplication of numbers
def multiply():
    # create another window for multiplication
    value_window = Toplevel(root_window)
    value_window.title("MULTIPLICATION")
    value_window.geometry("430x260")
    value_window.config(bg = "yellow")

    # set variables for first number
    first_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    first_num.place(x=200, y=10)

    # add label for first number
    note = Label(value_window, text = "Enter first number:", bg = "yellow", font=("Times", 15), justify = CENTER)
    note.place(x=10, y=10)

    # set variables for second number
    second_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    second_num.place(x=200, y=40)

    # add label for second number
    note1 = Label(value_window, text = "Enter second number:", bg = "yellow", font=("Times", 15), justify = CENTER)
    note1.place(x=10, y=40)

    # add label for result
    result = Label(value_window, text = "Result\t= ", bg = "yellow", font=("Times", 20), justify = CENTER)
    result.place(x=50, y=130)

    # add back button
    back_button = Button(value_window, text = "BACK", width = 20, command = value_window.destroy)
    back_button.place(x=225, y=200)

    # define clear
    def clear():
        first_num.delete(0, END)
        second_num.delete(0, END)

    # add clear button
    clear_button = Button(value_window, text = "CLEAR", width = 20, command = clear)
    clear_button.place(x=50, y=200)

    def multiply_1():
        try:
            total = float(first_num.get()) * float(second_num.get()) 
            entry.config(text = total)
        except:
            messagebox.showerror("ERROR", "ERROR! Invalid input!\n Please enter numbers only.")
    # entry
    entry = Label(value_window, text = "", bg = "yellow", font=("Times", 20), justify = CENTER)
    entry.place(x=200, y=130)

     # result button
    result_button = Button(value_window, text = "SHOW RESULT", width = 20, command = multiply_1)
    result_button.place(x=225, y=80)

# define a function for division of numbers
def divide():
    # create another window for division
    value_window = Toplevel(root_window)
    value_window.title("DIVISION")
    value_window.geometry("430x260")
    value_window.config(bg = "magenta")

    # set variables for first number
    first_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    first_num.place(x=200, y=10)

    # add label for first number
    note = Label(value_window, text = "Enter first number:", bg = "magenta", font=("Times", 15), justify = CENTER)
    note.place(x=10, y=10)

    # set variables for second number
    second_num = Entry(value_window, font=("Segoe Script",10), justify = CENTER)
    second_num.place(x=200, y=40)

    # add label for second number
    note1 = Label(value_window, text = "Enter second number:", bg = "magenta", font=("Times", 15), justify = CENTER)
    note1.place(x=10, y=40)

    # add label for result
    result = Label(value_window, text = "Result\t= ", bg = "magenta", font=("Times", 20), justify = CENTER)
    result.place(x=50, y=130)

    # add back button
    back_button = Button(value_window, text = "BACK", width = 20, command = value_window.destroy)
    back_button.place(x=225, y=200)

    # define clear
    def clear():
        first_num.delete(0, END)
        second_num.delete(0, END)

    # add clear button
    clear_button = Button(value_window, text = "CLEAR", width = 20, command = clear)
    clear_button.place(x=50, y=200)

    def divide_1():
        try:
            total = float(first_num.get()) / float(second_num.get()) 
            entry.config(text = total)
        except ZeroDivisionError:
            messagebox.showerror("ERROR", "Error: Division by zero is not allowed!!!")
        except:
            messagebox.showerror("ERROR", "ERROR! Invalid input!\n Please enter numbers only.")
    # entry
    entry = Label(value_window, text = "", bg = "magenta", font=("Times", 20), justify = CENTER)
    entry.place(x=200, y=130)

    # result button
    result_button = Button(value_window, text = "SHOW RESULT", width = 20, command = divide_1)
    result_button.place(x=225, y=80)   

# open a window using tkinter
root_window = Tk()
root_window.title("MINI CALCULATOR")
root_window.geometry("380x250")
root_window.config(bg = "brown")

# create welcoming text
Label(root_window, text = 'Welcome user!\n what would you like to do?', bg = "brown", fg = "white", font = ('Calibri', 15, 'bold')).pack(pady = 10)

# create buttons
# addition button
add_button = Button(root_window, text = "ADDITION", width = 20, command = addition)
add_button.place(x=30, y=90)
# subtraction button
subtract_button = Button(root_window, text = "SUBTRACTION", width = 20, command = subtract)
subtract_button.place(x=200, y=90)
# multiplication button
multiply_button = Button(root_window, text = "MULTIPLICATION", width = 20, command = multiply)
multiply_button.place(x=30, y=130)
# division button
division_button = Button(root_window, text = "DIVISION", width = 20, command = divide)
division_button.place(x=200, y=130)

# define function to exit
def exit_program():
    messagebox.askyesno("NOTICE", "You're about to exit the program?")
    root_window.quit()
# exit button
exit_button = Button(root_window, text = "EXIT", width = 20, command = exit_program)
exit_button.place(x=110, y=180)

# mainloop
root_window.mainloop()