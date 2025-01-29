import tkinter as tk
from tkinter import ttk, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("700x500")

        # Contact storage
        self.contacts = []

        # Heading
        tk.Label(root, text="Contact Book", font=("Arial", 18, "bold")).pack(pady=10)

        # Input Fields
        self.name_label = tk.Label(root, text="Name:", font=("Arial", 12))
        self.name_label.pack()
        self.name_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone:", font=("Arial", 12))
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(root, text="Email:", font=("Arial", 12))
        self.email_label.pack()
        self.email_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.email_entry.pack(pady=5)

        self.address_label = tk.Label(root, text="Address:", font=("Arial", 12))
        self.address_label.pack()
        self.address_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.address_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg="green", fg="white", font=("Arial", 12))
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, bg="orange", fg="white", font=("Arial", 12))
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, bg="red", fg="white", font=("Arial", 12))
        self.delete_button.pack(pady=5)

        # Contact List
        tk.Label(root, text="Contact List", font=("Arial", 14, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Search Functionality
        self.search_label = tk.Label(root, text="Search by Name or Phone:", font=("Arial", 12))
        self.search_label.pack(pady=5)
        self.search_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact, bg="blue", fg="white", font=("Arial", 12))
        self.search_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showerror("Input Error", "Name and Phone are required!")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        self.update_contact_list()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")

    def update_contact_list(self):
        self.tree.delete(*self.tree.get_children())
        for contact in self.contacts:
            self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")
            return

        selected_contact = self.tree.item(selected_item)["values"]
        self.contacts = [contact for contact in self.contacts if not (contact["Name"] == selected_contact[0] and contact["Phone"] == selected_contact[1])]
        self.update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def update_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")
            return

        selected_contact = self.tree.item(selected_item)["values"]
        self.name_entry.insert(0, selected_contact[0])
        self.phone_entry.insert(0, selected_contact[1])
        self.email_entry.insert(0, selected_contact[2])
        self.address_entry.insert(0, selected_contact[3])

        self.contacts = [contact for contact in self.contacts if not (contact["Name"] == selected_contact[0] and contact["Phone"] == selected_contact[1])]
        self.update_contact_list()

    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            messagebox.showwarning("Search Error", "Please enter a search query.")
            return

        results = [contact for contact in self.contacts if query in contact["Name"].lower() or query in contact["Phone"]]
        self.tree.delete(*self.tree.get_children())
        for contact in results:
            self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
