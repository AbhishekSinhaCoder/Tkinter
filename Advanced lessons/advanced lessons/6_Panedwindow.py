from tkinter import *
from tkinter import ttk 

window = Tk()
window.geometry('500x500')

Paned = ttk.Panedwindow(window, orien = HORIZONTAL)
Paned.pack()

frame1 = ttk.Frame(Paned, width = 200, height = 100, relief = RIDGE)
Paned.add(frame1)
frame2 = ttk.Frame(Paned, width = 500, height = 500, relief = RIDGE)
Paned.add(frame2, weight = 4)

frame3 = ttk.Frame(Paned, width = 500, height = 500, relief = RIDGE)
Paned.add(frame3, weight = 6)
window.mainloop()
