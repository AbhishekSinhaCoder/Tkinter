from tkinter import *

window = Tk()

window.geometry('500x500+300+400')
window.title('Hello world')
photo = PhotoImage(file=('1.gif'))
mbutton = Button(text='mahmoud raouf' , width=15 , height= 6 , fg='green' , bg='blue' , bd=15
                 , activebackground='green' , activeforeground='white', cursor= 'man'
                 , underline= 1, state=NORMAL, highlightthickness = 200
                 , image = photo).pack()




window.mainloop()
