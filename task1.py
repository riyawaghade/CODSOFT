import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")

        # Task list
        self.tasks = []

        # Heading
        self.heading_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
        self.heading_label.pack(pady=10)

        # Task entry
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task, bg="red", fg="white")
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed, bg="blue", fg="white")
        self.complete_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip() == "":
            messagebox.showwarning("Input Error", "Task cannot be empty!")
        else:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
        else:
            task_to_remove = selected_task_index[0]
            del self.tasks[task_to_remove]
            self.update_task_list()

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
        else:
            task_index = selected_task_index[0]
            self.tasks[task_index] += " (Completed)"
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
