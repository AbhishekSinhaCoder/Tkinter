import tkinter as tk
from tkinter import ttk

window = tk

def clickme():
    button.configure(text='Hello '+name.get())
    button.grid(column=1, row=1)


ttk.Label(text="Enter a name ").grid(column=0,row=0)

name = tk.StringVar()
entry = ttk.Entry(width=12, textvariable = name)
entry.grid(column=0, row=1)

button = ttk.Button(text='Clock Me', command=clickme)
button.grid(column=1,row=1)

window.mainloop()
