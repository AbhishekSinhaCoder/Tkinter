from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI")

        self.label = Label(master, text="Hallo Tkinter!")
        self.label.pack()

        self.greet_button = Button(master, text=" Welcome ", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print(" Welcome Python ")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
