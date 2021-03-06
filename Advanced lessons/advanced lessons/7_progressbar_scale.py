
from tkinter import *
from tkinter import ttk        
    
window = Tk()
window.geometry('600x100+400+300')

prog = ttk.Progressbar(window, orient = HORIZONTAL, length = 300)
prog.pack()
prog.config(maximum = 100, value = 25)
#prog.start()

value = DoubleVar()
prog.config(variable = value)
scale = ttk.Scale(window, orient = HORIZONTAL,
				  length = 250, variable = value,
				  from_ =0.0, to=100)
scale.pack()
scale.set(50)
window.mainloop()
