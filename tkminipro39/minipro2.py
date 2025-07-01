import tkinter as tk
from tkinter import messagebox, Text

def feedback_collector():
    def submit_feedback():
        messagebox.showinfo("Thanks", f"Thank you, {name.get()}!")
        name.delete(0, tk.END)
        comments.delete("1.0", tk.END)

    root = tk.Tk()
    root.title("Feedback Collector")

    tk.Label(root, text="Name").pack()
    name = tk.Entry(root)
    name.pack()

    tk.Label(root, text="Comments").pack()
    comments = Text(root, height=4, width=30)
    comments.pack()

    tk.Button(root, text="Submit", command=submit_feedback).pack()

    root.mainloop()

feedback_collector()

#     name.delete(0, tk.END)
#  – Clears the name entry field by deleting characters from position 0 to the end (tk.END).
#     comments.delete("1.0", tk.END)
# – Clears the comments Text box by deleting text from line 1, character 0 to the end.