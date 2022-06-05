import imp
from tkinter import *

from matplotlib.pyplot import fill

def upload():
    statusvar.set("Busy..")
    import time
    time.sleep(2)
    statusvar.set("Ready Now")


root = Tk()


root.title("Status bar")

root.geometry("644x255")


statusvar = StringVar()
statusvar.set("Ready Now")

sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill = X)

Button(root,text="upload",command=upload).pack()

















root.mainloop()