from tkinter import*
from tkinter import font
import tkinter

from setuptools import Command

root = Tk()

def getvals():
    print("Submitting the form")


    print(f"{namevalue.get(),gendervalue.get(),Emergency_contactvalue.get(),Payment_modevalue.get()}")

   
        # f.write(f"Name: {name.get()}\n")

    with open("record.txt","a") as f:
        f.write(f"Name: {namevalue.get()}\n")
        f.write(f"Gender: {gendervalue.get()}\n")
        f.write(f"Emergency_contactno: {Emergency_contactvalue.get()}\n")
        f.write(f"Payment_mode: {Payment_modevalue.get()}\n\n")
        f.close
        root.destroy
        


root.geometry("544x544")

#Heading

Label(root,text = "Welcome to Aryan Travel form",font="comicsansms 13 bold",justify=CENTER).grid(row=0 ,column=1)

#Text for our form

name = Label(root,text = "Name")

gender = Label(root,text = "Gender")

Emergency_contact = Label(root,text = "Emergency Contact")

Payment_mode = Label(root,text = "Payment Mode")

# pack text for our form

name.grid(row=1 ,column=0)
gender.grid(row=2 ,column=0)
Emergency_contact.grid(row=3 ,column=0)
Payment_mode.grid(row=4 ,column=0)

# Tkinter variable for storing entries  

namevalue = StringVar()
gendervalue = StringVar()
Emergency_contactvalue  = StringVar()
Payment_modevalue = StringVar() 

foodservicesvalue = IntVar()

# entry for the form
nameentry = Entry(root,textvariable=namevalue)
genderentry = Entry(root,textvariable=gendervalue)
emergencycontactentry = Entry(root,textvariable=Emergency_contactvalue)
paymentmodeentry = Entry(root,textvariable=Payment_modevalue) 


#packing the entry

nameentry.grid(row=1,column=1)
genderentry.grid(row=2,column=1) 
emergencycontactentry.grid(row=3,column=1)
paymentmodeentry.grid(row=4,column=1)

#checkbox

foodservice = Checkbutton(text = "Want to prebook your meals?",variable=foodservicesvalue)
foodservice.grid(row=5 ,column=1)

#button and packing it and assigning it a command

Button(text="Submit to Aryan travels",command =getvals).grid(row=7,column=0)



root.mainloop()