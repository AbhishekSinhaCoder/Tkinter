from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello world')
mbutton = Button(text="Hello world mahmoud").grid(row=1 , column=0)
mLabel = Label(text="Welcome", fg = 'red' ,bg= 'blue').grid(row=2 , column=1)

window.mainloop()
