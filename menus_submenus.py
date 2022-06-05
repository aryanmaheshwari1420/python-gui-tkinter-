from tkinter import *
root = Tk()

root.geometry("644x544")

root.title("menus_submenus")


def myfunc():
    print("hello world!")

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





















root.mainloop()