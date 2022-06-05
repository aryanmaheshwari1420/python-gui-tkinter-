from ctypes import alignment
from tkinter import *

from matplotlib import text
from numpy import pad

root = Tk()

root.geometry("454x456")

# root.minsize(200,100)
f1 = Frame(root,bg = "grey",borderwidth=6 , relief=GROOVE)
f1.pack(side=LEFT,fill ="y")

f2 = Frame(root,borderwidth=8,bg="grey",relief=GROOVE)
f2.pack(side=TOP,fill="x")


l1 = Label(f1,text="project tkinter - pycharm",font="helvetica",fg="red")
l2 = Label(f2,text="Welcome to Aryan project")
l1.pack(padx=20,pady=35)
l2.pack(pady=25)
root.mainloop()