from tkinter import *
# behaviour 1
t1 = Tk()
t1.geometry('400x400')

t1.b = Button(t1, text = "push me",
    command = lambda:t1.b.destroy())
t1.b.pack()
t1.mainloop()


