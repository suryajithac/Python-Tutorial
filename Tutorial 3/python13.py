
import tkinter as tk

def to_celsius():
    f = float(f_entry.get())
    c = (f - 32) * 5 / 9
    c_entry.delete(0, tk.END)
    c_entry.insert(0, str(round(c, 2)))

def to_fahrenheit():
    c = float(c_entry.get())
    f = c * 9 / 5 + 32
    f_entry.delete(0, tk.END)
    f_entry.insert(0, str(round(f, 2)))

win = tk.Tk()
win.title("Temperature Converter")

tk.Label(win, text="Fahrenheit").grid(row=0, column=0)
tk.Label(win, text="Celsius").grid(row=0, column=1)

f_entry = tk.Entry(win)
f_entry.grid(row=1, column=0)
f_entry.insert(0, "32")

c_entry = tk.Entry(win)
c_entry.grid(row=1, column=1)
c_entry.insert(0, "0.0")

tk.Button(win, text=">>>>", command=to_celsius).grid(row=2, column=0)
tk.Button(win, text="<<<<", command=to_fahrenheit).grid(row=2, column=1)

win.mainloop()
