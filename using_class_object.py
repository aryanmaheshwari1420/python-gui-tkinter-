from ast import If
from tkinter import *
from tkinter.tix import MAIN, WINDOW
from matplotlib.pyplot import text

class GUI(Tk):
    def __inti__(self):
        super().__init__()
        self.geometry("644x544")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvar =self.var,relief=  SUNKEN,anchor ="w")
        self.statusbar.pack(side=BOTTOM,pady=25,fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self,inptext):
        Button(text=inptext,command=self.click).pack()    


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.mainloop()

