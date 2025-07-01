import tkinter as tk
from tkinter import filedialog, messagebox

def load_file():
    file_path = path_entry.get()
    try:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[
        ("Text Files", "*.txt"),
        ("Python Files", "*.py"),
        ("CSV Files", "*.csv"),
        ("Log Files", "*.log"),
        ("All Files", "*.*")
    ])
    if file_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, file_path)

root = tk.Tk()
root.title("Text File Viewer")
root.geometry("600x400")

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

path_entry = tk.Entry(entry_frame, width=50)
path_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(entry_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack()

text_area = tk.Text(root, wrap="word", height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
