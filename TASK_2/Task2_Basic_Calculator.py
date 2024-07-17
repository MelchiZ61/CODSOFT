# Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers
# and an operation choice. Perform the calculation and display the result.

import tkinter as tk
from tkinter import Text

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.config(state="normal")
    text_result.delete("1.0", "end")
    text_result.insert("1.0", calculation)
    text_result.config(state="disabled")

#------------------------------------------
#------------------------------------------
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.config(state="normal")
        text_result.delete("1.0", "end")
        text_result.insert("1.0", calculation)
        text_result.config(state="disabled")
    except:
        clear_field()
        text_result.config(state="normal")
        text_result.insert("1.0", "Error")
        text_result.config(state="disabled")

#------------------------------------------
#------------------------------------------
def clear_field():
    global calculation
    calculation = ""
    text_result.config(state="normal")
    text_result.delete("1.0", "end")
    text_result.config(state="disabled")

#------------------------------------------
#------------------------------------------
root = tk.Tk()
root.title("Task 2: Basic Calculator Program")
root.geometry("480x560")
root.configure(background='#716565')

button_size = 100

text_result = Text(root, height=button_size * 2 // 30, width=button_size * 4 // 10, font=("Arial", 27)
                   , bg="#FFFDD0", fg="black")
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
text_result.config(state="disabled")

# configuring grid so that there is even spacing between the buttons
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

# Creating buttons
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
    ('(', 5, 0), ('0', 5, 1), (')', 5, 2), ('/', 5, 3),
    ('C', 6, 0), ('=', 6, 2)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear_field, height=button_size // 30, width=button_size * 2 // 10
                           , font=("Consolas", 30), fg="black", bg="#ADD8E6")
        button.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
    elif text == '=':
        button = tk.Button(root, text=text, command=evaluate_calculation, height=button_size // 30, width=button_size * 2 // 10
                           , font=("Consolas", 30), fg="black", bg="#ADD8E6")
        button.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), height=button_size // 30
                           , width=button_size // 10, font=("Times New Roman", 30), fg="black", bg="#ADD8E6")
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

root.mainloop()
#------------------------------------------
#------------------------------------------