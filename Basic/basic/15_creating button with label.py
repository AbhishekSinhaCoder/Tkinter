import tkinter as tk 
from tkinter import ttk 

window = tk
aLabel = ttk.Label(text="Tkinter") 
aLabel.grid(column=0, row=0)

def clickMe(): 
    button.configure(text="* The color has changed *")
    aLabel.configure(foreground='red')

button = ttk.Button(text="Click Me!", command=clickMe) 
button.grid(column=1, row=1)
window.mainloop()


