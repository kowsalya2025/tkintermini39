import tkinter as tk

root = tk.Tk()
root.title("Icon Test")

# Set icon (Windows only)
root.iconbitmap("logo.ico")  # Make sure it's an actual .ico file

# Task 15: Mix layout (Warning: Causes issues)
# You can uncomment below to observe error
mix_frame = tk.Frame(root)
mix_frame.pack()
tk.Label(mix_frame, text="Pack").pack()
tk.Entry(mix_frame).grid(row=0, column=0)  # Shouldn't mix pack and grid

root.mainloop()
