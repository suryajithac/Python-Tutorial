
import tkinter as tk

def replace_digits():
    text = entry.get()
    result.delete(0, tk.END)
    result.insert(0, ''.join('*' if ch.isdigit() else ch for ch in text))

win = tk.Tk()
win.title("Replace Digits")

entry = tk.Entry(win)
entry.pack()
result = tk.Entry(win)
result.pack()
tk.Button(win, text="Replace", command=replace_digits).pack()

win.mainloop()
