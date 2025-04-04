
import tkinter as tk

def to_upper():
    output.delete(0, tk.END)
    output.insert(0, entry.get().upper())

win = tk.Tk()
win.title("Uppercase Converter")

entry = tk.Entry(win)
entry.pack()
output = tk.Entry(win)
output.pack()
tk.Button(win, text="Convert", command=to_upper).pack()

win.mainloop()
