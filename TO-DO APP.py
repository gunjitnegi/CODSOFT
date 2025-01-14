import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operations.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Set up the main application window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("400x400")
app.configure(bg="#ADD8E6")  # Light Blue shade

# Title label
title_label = tk.Label(
    app, text="Simple Calculator", font=("Arial", 18, "bold"), bg="#ADD8E6", fg="#003366"
)
title_label.pack(pady=20)

# Number input labels and entries
label_num1 = tk.Label(app, text="Enter first number:", font=("Arial", 12), bg="#ADD8E6", fg="#003366")
label_num1.pack(pady=10)

entry_num1 = tk.Entry(app, font=("Arial", 14), width=20)
entry_num1.pack(pady=5)

label_num2 = tk.Label(app, text="Enter second number:", font=("Arial", 12), bg="#ADD8E6", fg="#003366")
label_num2.pack(pady=10)

entry_num2 = tk.Entry(app, font=("Arial", 14), width=20)
entry_num2.pack(pady=5)

# Operations dropdown
label_operation = tk.Label(app, text="Select operation:", font=("Arial", 12), bg="#ADD8E6", fg="#003366")
label_operation.pack(pady=10)

combo_operations = tk.StringVar()
operation_menu = tk.OptionMenu(app, combo_operations, "Add", "Subtract", "Multiply", "Divide")
operation_menu.config(font=("Arial", 14), width=15)
operation_menu.pack(pady=5)

# Calculate button
calc_button = tk.Button(app, text="Calculate", font=("Arial", 14), bg="#003366", fg="white", command=calculate)
calc_button.pack(pady=20)

# Result label
result_label = tk.Label(app, text="Result: ", font=("Arial", 14), bg="#ADD8E6", fg="#003366")
result_label.pack(pady=20)

# Run the application
app.mainloop()
