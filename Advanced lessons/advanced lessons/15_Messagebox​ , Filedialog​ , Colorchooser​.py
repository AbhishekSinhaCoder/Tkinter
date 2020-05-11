from tkinter import messagebox

messagebox.showinfo(title='Python', message='Hello Tkinter')
print(messagebox.askquestion(title='What do you want ?', message='Do you want open file ?'))

from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)

from tkinter import colorchooser
print(colorchooser.askcolor(initialcolor='#FFFFFF'))