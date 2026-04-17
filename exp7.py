import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conversion function
def convert():
    try:
        value = float(entry_value.get())
        conversion_type = combo_conversion.get()

        if conversion_type == "Rupees to Dollars":
            result = value / 92   # Approx conversion rate
            label_result.config(text=f"Result: {result:.2f} USD")

        elif conversion_type == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            label_result.config(text=f"Result: {result:.2f} °F")

        elif conversion_type == "Inches to Feet":
            result = value / 12
            label_result.config(text=f"Result: {result:.2f} ft")

        else:
            messagebox.showwarning("Selection Error", "Please select a conversion type")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Conversion Utilities")
root.geometry("350x300")
root.resizable(False, False)

# Heading
label_heading = tk.Label(root, text="Conversion Utilities", font=("Arial", 16, "bold"))
label_heading.pack(pady=10)

# Input value
label_value = tk.Label(root, text="Enter Value:")
label_value.pack()
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Conversion selection
label_conversion = tk.Label(root, text="Select Conversion Type:")
label_conversion.pack()

combo_conversion = ttk.Combobox(root,values=["Rupees to Dollars","Celsius to Fahrenheit","Inches to Feet"],state="readonly")
combo_conversion.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)

# Run application
root.mainloop()


"""import tkinter as tk

# Function to convert cm to inches
def convert_cm_to_inches():
    try:
        cm_value = float(entry_cm.get())
        inches = cm_value / 2.54   # 1 inch = 2.54 cm
        label_result.config(text=f"{cm_value:.2f} cm = {inches:.2f} inches")
    except ValueError:
        label_result.config(text="Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Simple Conversion GUI")
root.geometry("300x200")

# Heading
label_heading = tk.Label(root, text="CM to Inches Converter", font=("Arial", 14, "bold"))
label_heading.pack(pady=10)

# Input field
label_prompt = tk.Label(root, text="Enter length in cm:")
label_prompt.pack()
entry_cm = tk.Entry(root)
entry_cm.pack(pady=5)

# Button
button_convert = tk.Button(root, text="Convert", command=convert_cm_to_inches)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result will appear here", font=("Arial", 12))
label_result.pack(pady=10)

# Run application
root.mainloop()

USE THIS FOR SIMPLE ONE"""
