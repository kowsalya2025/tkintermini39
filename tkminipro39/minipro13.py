import tkinter as tk

def bmi_calculator():
    def calculate():
        try:
            h = float(height.get())
            w = float(weight.get())
            bmi = w / (h * h)
            result.set(f"BMI: {bmi:.2f}")
        except:
            result.set("Invalid Input")

    root = tk.Tk()
    root.title("BMI Calculator")

    height = tk.StringVar()
    weight = tk.StringVar()
    result = tk.StringVar()

    tk.Label(root, text="Height (m)").pack()
    tk.Entry(root, textvariable=height).pack()

    tk.Label(root, text="Weight (kg)").pack()
    tk.Entry(root, textvariable=weight).pack()

    tk.Button(root, text="Calculate BMI", command=calculate).pack()
    tk.Label(root, textvariable=result).pack()

    root.mainloop()

bmi_calculator()
