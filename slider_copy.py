from tkinter import *
import tkinter.messagebox as tmsg


def rateUs():
    if my_slider.get()>=7:
        tmsg.showinfo("Feedback", "Thank you for your feedback")
    
    elif my_slider.get()>=4:
        tmsg.showinfo("Feedback","We apologise for our poor service")
    
    elif my_slider.get()>=0:
        tmsg.showinfo("Feedback","We highly apologise for our poor service")

root= Tk()
root.geometry("1000x500")
root.title("Archan GUI")

Label(text= "\n\n\n\nHow Would you like to rate our service from 1-10\n", font= "comicsansms 10 bold").pack()

my_slider= Scale(root, from_=0, to= 10, orient= HORIZONTAL, tickinterval= 1, length=400)
my_slider.set(5)
my_slider.pack()

Label(text= "\n").pack()

Button(text= "Submit", font= "comicsansms 9 bold ", command= rateUs).pack()


root.mainloop()