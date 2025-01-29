import tkinter as tk
from tkinter import messagebox


class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x300")

        # Input fields for numbers
        self.label1 = tk.Label(root, text="Enter First Number:", font=("Arial", 12))
        self.label1.pack(pady=5)
        self.num1_entry = tk.Entry(root, width=20, font=("Arial", 12))
        self.num1_entry.pack(pady=5)

        self.label2 = tk.Label(root, text="Enter Second Number:", font=("Arial", 12))
        self.label2.pack(pady=5)
        self.num2_entry = tk.Entry(root, width=20, font=("Arial", 12))
        self.num2_entry.pack(pady=5)

        # Dropdown for operation selection
        self.label3 = tk.Label(root, text="Choose Operation:", font=("Arial", 12))
        self.label3.pack(pady=5)

        self.operation_var = tk.StringVar()
        self.operation_var.set("Add")  # Default option
        self.operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_menu = tk.OptionMenu(root, self.operation_var, *self.operations)
        self.operation_menu.pack(pady=5)

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate, bg="blue", fg="white", font=("Arial", 12))
        self.calculate_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 == 0:
                    messagebox.showerror("Error", "Division by zero is not allowed!")
                    return
                result = num1 / num2
            else:
                result = "Invalid Operation"

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers!")


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
