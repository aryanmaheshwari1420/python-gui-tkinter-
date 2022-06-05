from tkinter import *

def update():
    print("updating the gui")
    root.geometry(f"{height.get()}x{width.get()}")


root  = Tk()

root.geometry("644x544")


width = StringVar()
height = StringVar()


Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()

Button(root,text = "Apply",command=update).pack()

















root.mainloop()