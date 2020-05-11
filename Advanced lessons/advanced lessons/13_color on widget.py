
from tkinter import *

root= Tk()

frame_Toolbar = Frame(root,bg='Red', height=70)
frame_bootom = Frame(root,bg='green', height=20)
frame_Middle = Frame(root,bg='blue', height=250)


frame_Toolbar.pack(fill='x', side=TOP)
frame_bootom.pack(fill='x',side=BOTTOM)
frame_Middle.pack(side=TOP, fill=BOTH, expand=YES)
root.mainloop()