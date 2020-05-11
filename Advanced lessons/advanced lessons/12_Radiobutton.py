import tkinter as tk
from tkinter import ttk

window = tk.Tk()

def resCall():
    redSal = redVar.get()
    if redSal == 1:window.configure(background='Blue')
    elif redSal == 2:window.configure(background='Gold')
    elif redSal == 3:window.configure(background='Red')

redVar = tk.IntVar()

red1 = tk.Radiobutton(window,text='Blue',variable=redVar, value = 1, command=resCall)
red1.grid(column=0, row=0)
red2 = tk.Radiobutton(window,text='Gold',variable=redVar, value = 2, command=resCall)
red2.grid(column=0, row=1)
red3 = tk.Radiobutton(window,text='Red',variable=redVar, value = 3, command=resCall)
red3.grid(column=0, row=2)
window.mainloop()
