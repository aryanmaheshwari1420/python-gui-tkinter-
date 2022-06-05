
import tkinter.messagebox as tmg 

# for slider we use scale widget

from tkinter import *

root = Tk()

root.geometry("644x544")


root.title("Slider tutorial")


def getdollar():
    print(f"we have credited {myslider2.get()}dollar sto youyr bank account")
    tmg.showinfo("Amount Credited!",f"we have credited {myslider2.get()}dollar to your bank account")


# vertical slider

# myslider  = Scale(root , from_ =0 , to =455)
# myslider.pack()

# horizontal slider
Label(root, text = "how many dollar sdo you want?").pack()
myslider2  = Scale(root , from_ =0 , to =455 , orient=HORIZONTAL)
myslider2.pack()
Button(root,text = "Get dollars!",pady = 10,command= getdollar).pack()



















root.mainloop()