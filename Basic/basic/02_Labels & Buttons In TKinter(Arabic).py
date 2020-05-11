
from tkinter import *
window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')

mbutton = Button(text="Button").pack(pady=10)
mlabel = Label(text="Label",fg = 'red', bg = 'black').pack()

window.mainloop()
