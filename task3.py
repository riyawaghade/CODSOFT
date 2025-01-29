import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        # Heading
        self.heading_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
        self.heading_label.pack(pady=10)

        # Length Input
        self.length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root, width=10, font=("Arial", 12))
        self.length_entry.pack(pady=5)

        # Checkboxes for Complexity
        self.include_uppercase = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()

        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.pack()
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.pack()
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols)
        self.symbols_check.pack()

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="blue", fg="white")
        self.generate_button.pack(pady=10)

        # Display Password
        self.result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Input Error", "Password length must be at least 4!")
                return

            characters = string.ascii_lowercase  # Default: lowercase letters

            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += string.punctuation

            if not characters:
                messagebox.showwarning("Selection Error", "Please select at least one character type!")
                return

            password = ''.join(random.choices(characters, k=length))
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the length!")


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
