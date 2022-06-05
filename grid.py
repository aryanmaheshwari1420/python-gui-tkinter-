from tkinter import*
from tokenize import String

def get_value():
    print(f"The value of username is :{uservalue.get()}")
    print(f"The value of password is :{passvalue.get()}")



root = Tk()

root.geometry("454x484")

user = Label(root,text = "username")
password= Label(root,text="password")

user.grid()
password.grid(row=1)

# # Variable classes in tkinter

# BooleanVar , DoubleVar, IntVar , StringVar


uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable = uservalue)
passentry = Entry(root,textvariable = passvalue)

userentry.grid(row = 0 , column=1)
passentry.grid(row = 1 , column=1)


Button(text = "Submit" ,command = get_value).grid()

root.mainloop()


