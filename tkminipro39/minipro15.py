import tkinter as tk
from tkinter import messagebox

def quiz_app():
    question = "What is the capital of France?"
    correct_answer = "Paris"

    def check_answer():
        if answer.get().strip().lower() == correct_answer.lower():
            result.set("Correct!")
        else:
            result.set("Incorrect")

    root = tk.Tk()
    root.title("Basic Quiz App")

    tk.Label(root, text=question).pack()
    answer = tk.Entry(root)
    answer.pack()
    tk.Button(root, text="Submit", command=check_answer).pack()

    result = tk.StringVar()
    tk.Label(root, textvariable=result).pack()

    root.mainloop()

quiz_app()
