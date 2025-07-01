import tkinter as tk
from tkinter import messagebox

def login_form():
    def check_login():
        if username.get() == "admin" and password.get() == "1234":
            messagebox.showinfo("Login", "Welcome Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    root = tk.Tk()
    root.title("Login Form")

    tk.Label(root, text="Username").pack()
    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="Password").pack()
    password = tk.Entry(root, show="*")
    password.pack()

    tk.Button(root, text="Login", command=check_login).pack()

    root.mainloop()

login_form()
