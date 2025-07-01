import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import PhotoImage

# Task 1: Check Tkinter Installation (this script confirms it)
root = tk.Tk()

# Task 2, 3, 4: Basic Window with title and geometry
root.title("Tkinter Day34 Tasks")  # Task 2 & 3
root.geometry("500x500")  # Task 4


# Task 16, 31
# Frame for grouping widgets
frame1 = tk.Frame(root, borderwidth=2, relief="sunken")  
frame1.pack(pady=10)

# Task 5: Label
label = tk.Label(frame1, text="Welcome to Tkinter!", font=("Arial", 14), fg="green")  # Task 19
label.pack()

# Task 6, 22: Entry with default text
entry = tk.Entry(frame1)
entry.insert(0, "Enter your name")  # Task 22
entry.pack()

# Task 7, 8, 9, 20, 21, 28, 29, 34
def update_label(event=None):
    text = entry.get()
    if text.isdigit():
        label.config(text=f"Number entered: {text}")
    else:
        label.config(text=f"Text entered: {text}")

def toggle_button():
    if checkbox_var.get():
        btn.config(state="normal")
    else:
        btn.config(state="disabled")

def close_window():
    root.destroy()

btn = tk.Button(frame1, text="Click Me", command=update_label)
btn.pack()

# Task 29: Bind Enter key
root.bind('<Return>', update_label)

# Task 21: Checkbox to enable/disable button
checkbox_var = tk.BooleanVar(value=True)
check = tk.Checkbutton(frame1, text="Enable Button", variable=checkbox_var, command=toggle_button)
check.pack()

# Task 24: Set a window icon (optional and OS-dependent)
root.iconbitmap("logo.ico")  # Ensure icon.ico is in the same folder

# Task 25: Make window non-resizable
# root.resizable(False, False)

# Task 10, 11, 23, 30: Multi-line Text with Scrollbar
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget = tk.Text(text_frame, height=5, width=50, yscrollcommand=scrollbar.set)
text_widget.pack()

scrollbar.config(command=text_widget.yview)

def print_text():
    content = text_widget.get("1.0", tk.END).strip()
    print("Text Widget Content:\n", content)

def clear_widgets():
    entry.delete(0, tk.END)
    text_widget.delete("1.0", tk.END)

tk.Button(root, text="Print Text", command=print_text).pack()
tk.Button(root, text="Clear Text/Entry", command=clear_widgets).pack()

# Task 12: pack()
tk.Label(root, text="Packed 1").pack()
tk.Label(root, text="Packed 2").pack()
tk.Label(root, text="Packed 3").pack()

# Task 13: grid()
grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)
tk.Label(grid_frame, text="Grid Label").grid(row=0, column=0)
tk.Entry(grid_frame).grid(row=0, column=1)

# Task 14: place()
tk.Button(root, text="Placed Button").place(x=100, y=500)

# Task 15: Mix layout (Warning: Causes issues)
# You can uncomment below to observe error
# mix_frame = tk.Frame(root)
# mix_frame.pack()
# tk.Label(mix_frame, text="Pack").pack()
# tk.Entry(mix_frame).grid(row=0, column=0)  # Shouldn't mix pack and grid

# Task 17 & 18: Add Widgets to Multiple Frames
frame2 = tk.Frame(root, bg="lightgray")
frame2.pack(fill="x", pady=5)
tk.Label(frame2, text="Frame 2 Label").pack(side="left")
tk.Entry(frame2).pack(side="right")

frame3 = tk.Frame(root, bg="lightblue")
frame3.pack(fill="x", pady=5)
tk.Button(frame3, text="Frame 3 Button").pack()

# Task 27: Label with Image (Ensure image is present)
img = PhotoImage(file="cus.png")
tk.Label(root, image=img).pack()



# Task 32: pack(side=LEFT/RIGHT)
pack_side_frame = tk.Frame(root)
pack_side_frame.pack(pady=5)
tk.Label(pack_side_frame, text="Left").pack(side=tk.LEFT)
tk.Label(pack_side_frame, text="Right").pack(side=tk.RIGHT)

# Task 33: grid columnspan
span_frame = tk.Frame(root)
span_frame.pack(pady=5)
tk.Label(span_frame, text="Spanning Label").grid(row=0, column=0, columnspan=2)
tk.Entry(span_frame).grid(row=1, column=0)
tk.Entry(span_frame).grid(row=1, column=1)

# Task 26: Start maximized/minimized
# root.state('zoomed')  # Maximize (Windows)
# root.iconify()        # Minimize

# Task 34: Close Window Button
tk.Button(root, text="Exit App", command=close_window).pack(pady=10)

root.mainloop()
