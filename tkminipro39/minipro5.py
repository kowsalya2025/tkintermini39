import tkinter as tk

def todo_list():
    def add():
        tasks.insert(tk.END, entry.get())
        entry.delete(0, tk.END)

    def remove():
        tasks.delete(tk.ACTIVE)

    root = tk.Tk()
    root.title("To-Do List")

    entry = tk.Entry(root)
    entry.pack()

    tk.Button(root, text="Add Task", command=add).pack()
    tasks = tk.Listbox(root)
    tasks.pack()

    tk.Button(root, text="Remove Selected", command=remove).pack()
    root.mainloop()

todo_list()
