from tkinter import *
from tkinter import ttk 

window = Tk()
window.geometry('450x300')

frame =ttk.Frame(window)
frame.pack()

frame.config(height = 200, width = 400)
frame.config(relief = RIDGE)

ttk.Button(frame, text = 'Frame').pack()
frame.config(padding = (50,25))

ttk.LabelFrame(window, height = 200, width = 400, text='My Frame').pack()


window.mainloop()
