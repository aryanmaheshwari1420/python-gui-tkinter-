from tkinter import *

root = Tk()


def add():
    global i
    list_box.insert(ACTIVE , f"{i}") 
    # */ jo bhi list item hai vo uske upr jaake add ho jata hai/*
    i+=1

i=0
root.title("List box")

root.geometry("699x699")

list_box = Listbox(root)
list_box.pack()
list_box.insert(END,"First itemnof our listbox")

Button(root, text = "ADD iTEM",COMMAND = add).pack()


















root.mainloop()