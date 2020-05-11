from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello world')
mbutton = Button(text="Hello world mahmoud").grid(row=0 , column=0 )
mLabel = Label(text="Welcome", fg = '#000000' ,bg= '#f51BD4').grid(row=1 , column=0, sticky = E)

window.mainloop()
