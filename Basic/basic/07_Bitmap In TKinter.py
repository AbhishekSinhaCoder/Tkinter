from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello world')
# mLabel = Label(text="Welcome", fg = '#000000' ,bg= '#f51BD4').grid(row=1 , column=0, sticky = E)
mbutton = Button(text='Tkinter' , bitmap="error").pack()
mbutton = Button(text='Tkinter' , bitmap="hourglass").pack()
mbutton = Button(text='Tkinter' , bitmap="info").pack()
mbutton = Button(text='Tkinter' , bitmap="gray75").pack()
mbutton = Button(text='Tkinter' , bitmap="gray50").pack()
mbutton = Button(text='Tkinter' , bitmap="gray25").pack()
mbutton = Button(text='Tkinter' , bitmap="gray12").pack()
mbutton = Button(text='Tkinter' , bitmap="questhead").pack()
mbutton = Button(text='Tkinter' , bitmap="warning").pack()
mbutton = Button(text='Tkinter' , bitmap="question").pack()




window.mainloop()
