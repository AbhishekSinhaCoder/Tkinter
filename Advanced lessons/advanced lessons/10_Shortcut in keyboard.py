from tkinter import *
from tkinter import ttk        

def shortcut(action):
    print(action)
window = Tk()

window.bind('<Control-c>', lambda e: shortcut('Copy'))
window.bind('<Control-v>', lambda e: shortcut('Paste'))
window.bind('<Control-x>', lambda e: shortcut('Cut'))
window.bind('<Control-s>', lambda e: shortcut('Save'))

window.mainloop()
