from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello world')
mbutton = Button(text='Hello world ' , width=30 , height= 20 , bg='green' , fg='white' , bd=30
                 ,cursor= 'hand2', activebackground='red' , activeforeground='blue' ).pack()




window.mainloop()
