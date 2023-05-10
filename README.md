# About the program
a python program that serves as a mini calculator that can perform four mathematical operations (addition, subtraction, multiplication, and division).

## Procedural
1. Using the standard GUI library for python, a window was made with 5 buttons(ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, and EXIT)
2. Depending on what button the user will click another window frame will pop.
  ```python 
  add_button = Button(root_window, text = "ADDITION", width = 20, command = addition)
  subtract_button = Button(root_window, text = "SUBTRACTION", width = 20, command = subtract)
  multiply_button = Button(root_window, text = "MULTIPLICATION", width = 20, command = multiply)
  division_button = Button(root_window, text = "DIVISION", width = 20, command = divide)
  
  exit_button = Button(root_window, text = "EXIT", width = 20, command = exit_program)
  ```
3. After clicking one of the for mathematical operation, the user will be asked to input 2 numbers that will be computed based on the operation the user chose.
4. The result will be displayed after clicking the SHOW RESULT button.
  ```python 
  result_button = Button(value_window, text = "SHOW RESULT", width = 20, command = add)
  ```
5. The user can then decide whether to clear the numbers by clicking the CLEAR button or go back to the main window by clicking the BACK window.
6. If the user clicked the EXIT button the application will pop a message box confirming if the user wants to exit or not.
  
# Enjoy! 
