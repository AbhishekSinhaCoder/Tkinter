import tkinter as tk 
from tkinter import ttk
window = tk.Tk()

def clickme():
    button.configure(text='Hello '+name.get()+' '+number.get())


ttk.Label(text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(window, width=12, textvariable=number)
numberChosen['value']=(1,2,4,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current(3)



ttk.Label(text="Enter a name ").grid(column=0,row=0)
name = tk.StringVar()
entry = ttk.Entry(width=12, textvariable = name)
entry.grid(column=0, row=1)
button = ttk.Button(text='Clock Me', command=clickme)
button.grid(column=2,row=1)

window.mainloop()
