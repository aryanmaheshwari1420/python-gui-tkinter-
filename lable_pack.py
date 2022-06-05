from cProfile import label
from tkinter import *

from matplotlib import text
from matplotlib.pyplot import fill
from pandas import options
# from turtle import bgcolor
# from tkinter import font
# from webbrowser import BackgroundBrowser
# from numpy import tile

# from pyrsistent import T
root = Tk()

root.geometry("454x454")

root.title("AI BOT")

#Important Label options

# text = adds the text
# bd - Background
# fg - foreground
# font - sets the font
# padx - x _Padding
# pady - y _Padding
# relief - border styling  - SUNKEN , RAISED , GROOVE , RIDGE



title_label = Label(text="aryan is an good programmer",bg="grey")


# Important pack options
# anchor - NW
# side = top , bottom, left , right

title_label.pack(side =BOTTOM,anchor="sw",fill = X)
# fill = x --- agar window ko x ki taraf kheechenge toh khichta chala jaega similarly with y



root.mainloop()