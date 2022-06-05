from tkinter import *
from turtle import right

from matplotlib.pyplot import fill

root = Tk()

root.geometry("299x399")

root.title("Scroll bar")
# for connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

listbox = Listbox(root,yscrollcommand = scrollbar.set)
for i in range(344):
    listbox.insert(END ,f"Item{i}")

listbox.pack(fill="both",padx = 22)

text = Text(root,yscrollcommand = scrollbar.set)
text.pack(fill = BOTH)
scrollbar.config(command = listbox.yview)
scrollbar.config(command = text.yview)

root.mainloop()