import tkinter as tk

def basic_calculator():
    def click(char):
        entry.insert(tk.END, char)

    def calculate():
        try:
            result.set(str(eval(entry.get())))
        except:
            result.set("Error")

    def clear():
        entry.delete(0, tk.END)
        result.set("")

    root = tk.Tk()
    root.title("Basic Calculator")

    result = tk.StringVar()
    entry = tk.Entry(root)
    entry.pack()
    tk.Label(root, textvariable=result).pack()

    buttons = ["123", "456", "789", "0+-", "*/="]
    for row in buttons:
        frame = tk.Frame(root)
        frame.pack()
        for ch in row:
            if ch == "=":
                tk.Button(frame, text=ch, command=calculate).pack(side=tk.LEFT)
            else:
                tk.Button(frame, text=ch, command=lambda c=ch: click(c)).pack(side=tk.LEFT)

    tk.Button(root, text="Clear", command=clear).pack()
    root.mainloop()

basic_calculator()
