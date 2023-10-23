# Importing GUI (tkinter, ttk) and time modules
import tkinter as tk
from tkinter import ttk
import time

# Function to handle button click, update the entry field and animate the button
def button_click(number):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
    animate_button(number)

def animate_button(number):
    button = button_mapping[number]
    original_bg = button.cget('background')
    new_bg = 'blue'
    
    for _ in range(2):
        button.configure(background=new_bg)
        root.update()
        time.sleep(0.1)
        button.configure(background=original_bg)
        root.update()
        time.sleep(0.1)

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression in the entry field and display the result or an error message
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Initializing the Tkinter window and setting its title to "Calculator"
root = tk.Tk()
root.title("Calculator")

# Change the background color to black
root.configure(bg='black')

# Creating an entry field in the Tkinter window and a list of buttons for the calculator
entry = tk.Entry(root, width=16, font=('Consolas', 24), bd=5, justify='right', bg='white', fg='black')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '%'
]

row_val = 1
col_val = 0

button_mapping = {}

for button in buttons:
    btn = ttk.Button(root, text=button, padding=20, style='Calculator.TButton',
                     command=lambda button=button: button_click(button))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    button_mapping[button] = btn
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Adjust the "=" button to span all four columns
equal_button = ttk.Button(root, text='=', padding=20, style='Calculator.TButton',
                          command=button_equal)
equal_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

clear_button = ttk.Button(root, text='C', padding=20, style='Calculator.TButton',
                         command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# Customize the appearance
root.configure(bg='grey')
entry.configure(fg='black')

# Create a custom style for the buttons to change the background color on hover
style = ttk.Style()
style.configure('Calculator.TButton', background='light gray')

# Run the GUI application
root.mainloop()
