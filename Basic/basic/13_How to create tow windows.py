from tkinter import *
Old = Tk()
new = Tk()
def hello():
    m = a.get()
    myLabel = Label(new, text= m , fg = 'red', bg='black',font=10).pack()

def delete():
    myLabel2 = Label(new, text='deleted', fg='red', bg='yellow',font= 10).pack()

a = StringVar()
Old.title("Hello")
new.title("Hello")

Old.geometry("400x400+100+50")
new.geometry("400x400+600+50")

myLabel = Label(Old, text='enter' , fg='red', bg='gray', font=10).pack()
myButton1 = Button(Old, text='enter', fg='black', bg='gray',command = hello, font=20).pack()
myButton2 = Button(new, text='deleted', fg='black', bg='gray',command = delete, font=20).pack()
text = Entry(Old, textvariable = a).pack()

Old.mainloop()
