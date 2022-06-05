from tkinter import *
from turtle import position
 
def Aryan(event):
    print(f"wonderful! you succesfully pass the test case{event.x},{event.y}") 

root = Tk()

root.title("Events in Tkinter")
root.geometry("644x544")

widget = Button(root,text  = "click me please")
widget.pack()

widget.bind('<Button-1>',Aryan)
widget.bind('<Double-1>',quit) # on double click it will quit the window










root.mainloop()