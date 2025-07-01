import tkinter as tk

def word_counter():
    def count():
        text_content = text.get("1.0", tk.END)
        words = text_content.split()
        result.set(f"Word Count: {len(words)}")

    root = tk.Tk()
    root.title("Word Counter")

    text = tk.Text(root, height=10, width=40)
    text.pack()

    tk.Button(root, text="Count Words", command=count).pack()
    result = tk.StringVar()
    tk.Label(root, textvariable=result).pack()

    root.mainloop()

word_counter()
