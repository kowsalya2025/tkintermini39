import tkinter as tk

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts.append(f"{name} - {phone}")
        display_contacts()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

def display_contacts():
    contact_display.delete("1.0", tk.END)
    for contact in contacts:
        contact_display.insert(tk.END, contact + "\n")

# Main Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x350")

# Name Entry
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Phone Entry
tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

# Add Button
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=10)

# Contacts Display
tk.Label(root, text="Saved Contacts").pack()
contact_display = tk.Text(root, height=10, width=40)
contact_display.pack(pady=5)

root.mainloop()
