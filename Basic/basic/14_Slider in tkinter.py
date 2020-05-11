import tkinter as tk

master = tk.Tk()
w2 = tk.Scale(master, from_=10, to=64)
w2.set(22)
w2.pack()
w1 = tk.Scale(master, from_=0, to=300)
w1.pack()
master.mainloop()
