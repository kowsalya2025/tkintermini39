import tkinter as tk
from tkinter import messagebox

def survey_app():
    def submit():
        messagebox.showinfo("Survey Submitted",f"Name: {name.get()}\nAge: {age.get()}\nColor: {color.get()}")
       

    root = tk.Tk()
    root.title("Simple Survey App")

    name = tk.StringVar()
    age = tk.StringVar()
    color = tk.StringVar()

    tk.Label(root, text="Name").pack()
    tk.Entry(root, textvariable=name).pack()

    tk.Label(root, text="Age").pack()
    tk.Entry(root, textvariable=age).pack()

    tk.Label(root, text="Favorite Color").pack()
    tk.Entry(root, textvariable=color).pack()

    tk.Button(root, text="Submit", command=submit).pack()

    root.mainloop()

survey_app()
