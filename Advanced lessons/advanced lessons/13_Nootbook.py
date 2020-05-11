from tkinter import *
from tkinter import ttk

root = Tk()

note = ttk.Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)

ttk.Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=200)

note.add(tab1, text='Tab One')
note.add(tab2, text='Tab Tow')
note.add(tab3, text='Tab Three')

note.pack()

root.mainloop()
