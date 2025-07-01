import tkinter as tk
from tkinter import Text

def temperature_logger():
    def log():
        log_area.insert(tk.END, f"{temp.get()} °C\n")
        temp.delete(0, tk.END)

    root = tk.Tk()
    root.title("Temperature Logger")

    temp = tk.Entry(root)
    temp.pack()
    tk.Button(root, text="Log Temperature", command=log).pack()

    log_area = Text(root, height=6, width=30)
    log_area.pack()

    root.mainloop()

temperature_logger()
