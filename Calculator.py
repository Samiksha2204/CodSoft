import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Division by zero is not allowed")
            result = num1 / num2
        else:
            result = "Invalid operation"
        
        label_result.config(text=f"Result: {result}")
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='lightyellow')  


label_num1 = tk.Label(root, text="Enter first number:", bg='lightgreen')
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:", bg='lightgreen')
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Select operation:", bg='lightgreen')
label_operation.grid(row=2, column=0, padx=10, pady=10)

operation_var = tk.StringVar(value='+')
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=2, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, columnspan=2, pady=10)

label_result = tk.Label(root, text="Result: ", bg='lightblue')
label_result.grid(row=4, columnspan=2, pady=10)


root.mainloop()
