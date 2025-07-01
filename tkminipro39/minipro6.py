import tkinter as tk
import time

def digital_clock():
    def update():
        time_var.set(time.strftime("%H:%M:%S"))
        root.after(1000, update)

    root = tk.Tk()
    root.title("Digital Clock")

    time_var = tk.StringVar()
    tk.Label(root, textvariable=time_var, font=("Arial", 30)).pack()

    update()
    root.mainloop()

digital_clock()
