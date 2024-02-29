import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class Contact_book:
    def __init__(self, root):
        self.root = root
        root.resizable(False, False)
        self.contacts = []

        self.root.title("Contact Organizer")

        self.name_label = tk.Label(root, text="Full Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(root, text="Email Address:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(root, text="Home Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Save Contact", command=self.save_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.view_button = tk.Button(root, text="View All Contacts", command=self.view_all_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.search_label = tk.Label(root, text="Search Contact:")
        self.search_label.grid(row=6, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def save_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact saved successfully.")

    def view_all_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact List", "No contacts available.")
        else:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        keyword = self.search_entry.get().lower()
        results = [contact for contact in self.contacts if keyword in contact.name.lower() or keyword in contact.phone_number]
        if not results:
            messagebox.showinfo("Search Results", "No match.")
        else:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}" for contact in results])
            messagebox.showinfo("Search Results", contact_list)

def main():
    root = tk.Tk()
    app = Contact_book(root)
    root.mainloop()

if __name__ == "__main__":
    main()
