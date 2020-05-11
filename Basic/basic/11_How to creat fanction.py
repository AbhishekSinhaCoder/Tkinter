from tkinter import *
myGui = Tk()


def hello():
    myLabel = Label(text='enter' , fg = 'yellow', bg='orange',font=10).pack()
    
def delete():
    myLabel2 = Label(text='delete', fg='orange', bg='yellow',font= 10).pack()
    

myGui.title("Hello")
myGui.geometry("500x300+300+400")
myLabel = Label(text='Welcome' , fg='#646060', bg='#F87217', font=10).pack()
myButton1 = Button(text='enter', fg='gray', bg='plum',command = hello, font=20).pack()
myButton2 = Button(text='deleted', fg='gray', bg='plum',command = delete, font=20).pack()


myGui.mainloop()
