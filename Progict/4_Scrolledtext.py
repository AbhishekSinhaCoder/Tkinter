import tkinter as tk 
from tkinter import ttk
window = tk.Tk()

def clickMe():
    button.configure(text='Hello ' + name.get()+ ' ' + number.get())


ttk.Label(text="Choose a number:").grid(column=1, row=0)

number = tk.StringVar()
numberChosen = ttk.Combobox(window, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(2)


ttk.Label(window, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
button = ttk.Button(window, text="Click Me!", command=clickMe)
button.grid(column=2, row=1)

check1 = tk.Checkbutton(window, text="Disabled", state
='disabled')
check1.select()
check1.grid(column=0, row=2)

check2 = tk.Checkbutton(window, text="UnChecked")
check2.deselect()
check2.grid(column=1, row=2)

check3 = tk.Checkbutton(window, text="Enabled")
check3.select()
check3.grid(column=2, row=2)

from tkinter import scrolledtext
scrolW= 30
scrolH= 10
scr = scrolledtext.ScrolledText(window, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3)

window.mainloop()
