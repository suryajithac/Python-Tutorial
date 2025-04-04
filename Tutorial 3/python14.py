
import tkinter as tk

def count_vowels():
    text = entry.get().lower()
    count = sum(1 for ch in text if ch in "aeiou")
    result.delete(0, tk.END)
    result.insert(0, f"Vowels: {count}")

win = tk.Tk()
win.title("Vowel Counter")

entry = tk.Entry(win)
entry.pack()
result = tk.Entry(win)
result.pack()
tk.Button(win, text="Count Vowels", command=count_vowels).pack()

win.mainloop()
