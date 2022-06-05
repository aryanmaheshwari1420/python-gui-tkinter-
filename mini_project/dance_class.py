from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Dance Form")

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN, padx=23, pady=46)
f1.pack()

Label(f1, text="Dance Academy Form", font="helvetica 20 bold underline", pady=4, padx=25, fg="grey",
      bg="black", relief=SUNKEN).grid(column=1)

name = Label(f1, text="Name: ",bg="grey").grid(row=8,column=0)
dob = Label(f1, text="DOB: ",bg="grey").grid(row=9)
age = Label(f1, text="Age: ",bg="grey").grid(row=10)

name = StringVar()
dob = StringVar()
age = StringVar()

name_entry = Entry(f1, textvariable=name)
dob_entry = Entry(f1, textvariable=dob)
age_entry = Entry(f1, textvariable=age)

name_entry.grid(row=8, column=1)
dob_entry.grid(row=9, column=1)
age_entry.grid(row=10, column=1)


def save():
    f = open("form.txt", "a")
    f.write(f"Name: {name.get()}\n")
    f.write(f"DOB: {dob.get()}\n")
    f.write(f"Age: {age.get()}\n\n")
    f.close()
    root.destroy()


Button(f1, text="Submit", command=save).grid(column=1)

root.mainloop()