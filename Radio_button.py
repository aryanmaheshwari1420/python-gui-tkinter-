from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import text

import tkinter.messagebox as tmg
root = Tk()

root.geometry("644x544")


root.title("Radio_button")



def order():
    print("Feedback", "Thank you for your feedback")
    tmg.showinfo("Received", f" order has been confirmed of your {var.get()} \n\n thank you for ordering")



var = IntVar()
var = StringVar()
var.set(1)

Label(root,text ="What would you like to have sir?",font="lucida 19 bold",justify = CENTER,padx =14).pack()


radio = Radiobutton(root,text="DOSA",padx =14, variable=var,value="dosa").pack(anchor="w")
radio = Radiobutton(root,text="sambar",padx =14, variable=var,value="sambar").pack(anchor="w")
radio = Radiobutton(root,text="Idly",padx =14, variable=var,value="idly").pack(anchor="w")
radio = Radiobutton(root,text="utpam",padx =14, variable=var,value="utpam").pack(anchor="w")
radio = Radiobutton(root,text="vada",padx =14, variable=var,value="vada").pack(anchor="w")


Button(text = "submit",command=order).pack()






































root.mainloop()
