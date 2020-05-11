from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello world')
# mLabel = Label(text="Welcome", fg = '#000000' ,bg= '#f51BD4').grid(row=1 , column=0, sticky = E)
mbutton = Button(text='Hello Tkinter' , relief=SUNKEN ).pack()
mbutton = Button(text='Hello Tkinter' , relief= FLAT).pack()
mbutton = Button(text='Hello Tkinter' , relief= GROOVE).pack()
mbutton = Button(text='Hello Tkinter' , relief= RAISED).pack()
mbutton = Button(text='Hello Tkinter' , relief= RIDGE).pack()



window.mainloop()
