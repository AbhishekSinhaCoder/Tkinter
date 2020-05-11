from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello world')
mbutton = Button(text="Hello world").place(x =150 , y =120)
mLabel = Label(text="Welcome", fg = 'red' ,bg= 'blue').place(x = 200, y = 200)

window.mainloop()
