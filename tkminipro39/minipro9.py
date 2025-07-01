import tkinter as tk
from tkinter import messagebox
import random

def guess_the_number():
    target = random.randint(1, 100)

    def check():
        try:
            guess = int(entry.get())
            if guess < target:
                result.set("Too Low")
            elif guess > target:
                result.set("Too High")
            else:
                result.set("Correct!")
        except:
            result.set("Enter a number")

    def reset():
        nonlocal target
        target = random.randint(1, 100)
        entry.delete(0, tk.END)
        result.set("")

    root = tk.Tk()
    root.title("Guess the Number")

    tk.Label(root, text="Guess a number between 1 and 100").pack()
    entry = tk.Entry(root)
    entry.pack()

    tk.Button(root, text="Submit Guess", command=check).pack()

    result = tk.StringVar()
    tk.Label(root, textvariable=result).pack()
    tk.Button(root, text="Reset Game", command=reset).pack()

    root.mainloop()

guess_the_number()
