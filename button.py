from distutils import command
from tkinter import *

root = Tk()

root.geometry("454x456")


def printing():
    print("your matter has been printed")



frame  = Frame(root,borderwidth=6,bg="grey",relief=GROOVE)
frame.pack(side =LEFT,anchor="nw")

b1 = Button(frame,fg="red",text="print now",command=printing)
b1.pack(side=LEFT,padx=23)

b2 = Button(frame,fg="green",text="sign in")
b2.pack(side=LEFT,padx=23)

b3= Button(frame,fg="blue",text="log in")
b3.pack(side=LEFT,padx=23)


root.mainloop()
