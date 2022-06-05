from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("644x544")

root.title("menus_submenus")


def myfunc():
    print("hello world!")

def help():
    print("I will help you dont't worry")
    a= tmsg.showinfo("help","harry will help you with this gui")


def rate():
    print("rate done")
    value = tmsg.askquestion("how was your experience","how was your gui experience")
    # print(value)
    if value == "yes":
        msg = "Great Rate us on the appstore plz!"
    else:
        msg = "Tell us want went wrong we u call u soon"  
    tmsg.showinfo("Experience",msg)      


def divya():
    ans = tmsg.askretrycancel("divya se dosti kar lo","soorry divya nahi pategi")
    if ans:
        print("retry krne pe kuch nahi hoga")
    else:
        print("bach gya pit jaata varna")    
# use these to create a non dropdown menu

# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="File",command=quit)
# root.config(menu=mymenu)


# use this to create a dropdown menu

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_separator()
m1.add_command(label="Print",command=myfunc)
m1.add_command(label="New Project",command=myfunc)

mainmenu.add_cascade(label ="file",menu=m1)
root.config(menu=mainmenu)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Save",command=myfunc)
m2.add_command(label="Save As",command=myfunc)
m2.add_separator()
m2.add_command(label="Print",command=myfunc)
m2.add_command(label="New Project",command=myfunc)

mainmenu.add_cascade(label ="Edit",menu=m2)
root.config(menu=mainmenu)


m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Save As",command=help)
m3.add_command(label="rate us",command=rate)
m3.add_command(label="befriend",command=divya)
mainmenu.add_cascade(label ="help",menu=m3)
root.config(menu=mainmenu)
















root.mainloop()