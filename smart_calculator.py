import math
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def addition():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform subtraction
def subtraction():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform multiplication
def multiplication():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform division
def division():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to calculate root
def calculate_root():
    try:
        num1 = float(num1_entry.get())
        root = float(num2_entry.get())
        result = num1 ** (1 / root)
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to calculate power
def calculate_power():
    try:
        num1 = float(num1_entry.get())
        power = float(num2_entry.get())
        result = num1 ** power
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to calculate the number of days between dates
def days_between_dates():
    try:
        date_format = "%d-%m-%Y"
        date1 = date1_entry.get()
        date2 = date2_entry.get()
        datetime1 = datetime.strptime(date1, date_format)
        datetime2 = datetime.strptime(date2, date_format)
        delta = datetime2 - datetime1
        result = delta.days
        result_label.config(text="Number of days: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter dates in DD-MM-YYYY format.")

# Function to solve a quadratic equation
def solve_quadratic():
    try:
        try:
            a = float(num1_entry.get())
        except:
            a = 0
        try:
            b = float(num2_entry.get())
        except:
            b = 0
        try:
            c = float(num3_entry.get())
        except:
            c = 0
        
        if (a == 0):
            result = -c / b
            result_label.config(text=result)
            return
        
        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # Check the nature of roots
        if discriminant > 0:
            # Two real and distinct roots
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            result = "Roots: " + str(root1) + ", " + str(root2)
        elif discriminant == 0:
            # Two real and identical roots
            root = -b / (2*a)
            result = "Root: " + str(root)
        else:
            # Complex roots
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            root1 = str(real_part) + " + " + str(imaginary_part) + "i"
            root2 = str(real_part) + " - " + str(imaginary_part) + "i"
            result = "Roots: " + root1 + ", " + root2

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid coefficients.")

# Create the main Tkinter window
window = tk.Tk()
window.title("Smart Calculator")

# Create the labels and entry fields
num1_label = tk.Label(window, text="Number 1:")
num1_label.grid(row=0, column=0, padx=10, pady=10)
num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1, padx=10, pady=10)

num2_label = tk.Label(window, text="Number 2:")
num2_label.grid(row=1, column=0, padx=10, pady=10)
num2_entry = tk.Entry(window)
num2_entry.grid(row=1, column=1, padx=10, pady=10)

num3_label = tk.Label(window, text="Number 3:")
num3_label.grid(row=2, column=0, padx=10, pady=10)
num3_entry = tk.Entry(window)
num3_entry.grid(row=2, column=1, padx=10, pady=10)

date1_label = tk.Label(window, text="Date 1 (DD-MM-YYYY):")
date1_label.grid(row=3, column=0, padx=10, pady=10)
date1_entry = tk.Entry(window)
date1_entry.grid(row=3, column=1, padx=10, pady=10)

date2_label = tk.Label(window, text="Date 2 (DD-MM-YYYY):")
date2_label.grid(row=4, column=0, padx=10, pady=10)
date2_entry = tk.Entry(window)
date2_entry.grid(row=4, column=1, padx=10, pady=10)

result_label = tk.Label(window, text="Result:", font=("Helvetica", 16, "bold"))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create the buttons
add_button = tk.Button(window, text="Addition", command=addition, padx=10, pady=5, width=15)
add_button.grid(row=6, column=0, padx=10, pady=10)

subtract_button = tk.Button(window, text="Subtraction", command=subtraction, padx=10, pady=5, width=15)
subtract_button.grid(row=6, column=1, padx=10, pady=10)

multiply_button = tk.Button(window, text="Multiplication", command=multiplication, padx=10, pady=5, width=15)
multiply_button.grid(row=7, column=0, padx=10, pady=10)

divide_button = tk.Button(window, text="Division", command=division, padx=10, pady=5, width=15)
divide_button.grid(row=7, column=1, padx=10, pady=10)

power_button = tk.Button(window, text="Power", command=calculate_power, padx=10, pady=5, width=15)
power_button.grid(row=8, column=0, padx=10, pady=10)

days_button = tk.Button(window, text="Days Between Dates", command=days_between_dates, padx=10, pady=5, width=15)
days_button.grid(row=8, column=1, padx=10, pady=10)

quadratic_button = tk.Button(window, text="Quadratic Equation", command=solve_quadratic, padx=10, pady=5, width=30)
quadratic_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Run the main Tkinter event loop
window.mainloop()