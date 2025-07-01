import tkinter as tk

def unit_converter():
    def convert():
        try:
            val = float(entry.get())
            if var.get() == "cm to inch":
                out.set(f"{val / 2.54:.2f} inches")
            else:
                out.set(f"{val * 2.54:.2f} cm")
        except:
            out.set("Invalid")

    root = tk.Tk()
    root.title("Unit Converter")

    var = tk.StringVar(value="cm to inch")
    entry = tk.Entry(root)
    entry.pack()

    tk.OptionMenu(root, var, "cm to inch", "inch to cm").pack()
    tk.Button(root, text="Convert", command=convert).pack()

    out = tk.StringVar()
    tk.Label(root, textvariable=out).pack()

    root.mainloop()

unit_converter()
