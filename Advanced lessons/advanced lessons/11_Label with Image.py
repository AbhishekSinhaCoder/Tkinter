
from tkinter import *
from tkinter import ttk        
    
window = Tk()

label = ttk.Label(window, text='Hello Tkinter')
label.pack()
label.config(foreground = 'silver' , background='brown')
label.config(font =('Aria', 20, 'bold'))

label.config(wraplength=100)
label.config(justify= CENTER)

logo = PhotoImage(file = 'python tkinter.gif')
label.config(image = logo)
label.config(compound ='left')

window.mainloop()
