import tkinter as tk
from tkinter import messagebox

def address_form():
    def display():
        messagebox.showinfo("Address Info",
                            f"Name: {name.get()}\nAddress: {address.get()}\nPhone: {phone.get()}")

    root = tk.Tk()
    root.title("Address Form")

    name = tk.StringVar()
    address = tk.StringVar()
    phone = tk.StringVar()

    tk.Label(root, text="Name").pack()
    tk.Entry(root, textvariable=name).pack()

    tk.Label(root, text="Address").pack()
    tk.Entry(root, textvariable=address).pack()

    tk.Label(root, text="Phone").pack()
    tk.Entry(root, textvariable=phone).pack()

    tk.Button(root, text="Submit", command=display).pack()

    root.mainloop()

address_form()
