import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
      
        self.name_entry = self.create_entry("Name", 0)
        self.phone_entry = self.create_entry("Phone Number", 1)
        self.email_entry = self.create_entry("Email", 2)
        self.address_entry = self.create_entry("Address", 3)
        
    
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)
        
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1, padx=10, pady=10)
        
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=2, padx=10, pady=10)
        
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=4, column=3, padx=10, pady=10)
        
 
        self.contact_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contact_listbox.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
        self.update_contact_list()

    def create_entry(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(self.root, width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            self.contacts[phone] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
            self.update_contact_list()
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def update_contact(self):
        selected_contact = self.contact_listbox.curselection()
        if selected_contact:
            phone = self.contact_listbox.get(selected_contact).split(" - ")[1]
            name = self.name_entry.get()
            new_phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            
            if new_phone:
                self.contacts.pop(phone)
                self.contacts[new_phone] = {"name": name, "email": email, "address": address}
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                self.update_contact_list()
            else:
                messagebox.showwarning("Input Error", "Phone number is required.")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_contact = self.contact_listbox.curselection()
        if selected_contact:
            phone = self.contact_listbox.get(selected_contact).split(" - ")[1]
            self.contacts.pop(phone)
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.update_contact_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def search_contact(self):
        search_query = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if search_query:
            results = {phone: details for phone, details in self.contacts.items() if search_query.lower() in details["name"].lower() or search_query in phone}
            self.update_contact_list(results)
        else:
            self.update_contact_list()

    def update_contact_list(self, contacts=None):
        self.contact_listbox.delete(0, tk.END)
        if contacts is None:
            contacts = self.contacts
        for phone, details in contacts.items():
            self.contact_listbox.insert(tk.END, f"{details['name']} - {phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
