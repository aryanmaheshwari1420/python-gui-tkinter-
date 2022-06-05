from email.mime import image
from tkinter import *
from PIL import Image  , ImageTk

aryan_root = Tk()

aryan_root.geometry("454x244")

photo = PhotoImage(file="yannes-kiefer-ZpJXCNAAUPY-unsplash.png")

#for jpg images

# image = Image.open("photo.jpg")
# photo = Imagetk.PhotoImage(image)

vishu_label = Label(aryan_root , image=photo)

vishu_label.pack() # to see in the gui window we have do it

aryan_root.mainloop()