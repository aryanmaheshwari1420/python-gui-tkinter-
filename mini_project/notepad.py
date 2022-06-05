from cProfile import label
from fileinput import filename
from msilib.schema import File
from pickle import GLOBAL
from tkinter import *
from tkinter.tix import FileEntry
from turtle import right

from numpy import size
import os
from tkinter.messagebox import showinfo

from tkinter.filedialog import askopenfilename, asksaveasfilename

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textarea.delete(1.0,END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        Textarea.delete(1.0,END)
        f = open(file,"r")
        Textarea.insert(1.0,f.read())  
        f.close()  


def savefile():
    global file
    if file ==None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])

        if file == "":
            file = None
        else:
            # save as a new file  
            f = open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ " -Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file , "w")
        f.write(Textarea.get(1.0 , END))
        f.close()




def quitapp():
    root.destroy()

def cut():
    Textarea.event_generate(("<<Cut>>"))

def copy():
    Textarea.event_generate(("<<Copy>>"))

def paste():
    Textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Code with Harry")

if __name__ == '__main__':
    # basic tkinter setup

    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x588")


    #add textarea
    Textarea = Text(root, font ="lucida 13")
    file = None
    Textarea.pack(expand = True , fill = BOTH)
    # lets create a menubar
    Menubar = Menu(root)
    # file menu starts
    Filemenu = Menu(Menubar,tearoff = 0)
    # to open new file
    Filemenu.add_command(label = "New",command=newFile)

    #To open already existing file

    Filemenu.add_command(label="Open",command=openFile)

    # to save the current file

    Filemenu.add_command(label = "save", command=savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label = "exit ", command =quitapp)
    Menubar.add_cascade(label = "File",menu = Filemenu)
    # file menu ends

    # edit menu starts
    Editmenu = Menu(Menubar,tearoff = 0)
    # To give a feature of cut , copy and paste

    Editmenu.add_command(label = "cut", command=cut)
    Editmenu.add_command(label = "copy", command=copy)
    Editmenu.add_command(label = "paste", command=paste)

    Menubar.add_cascade(label = "Edit",menu =Editmenu)
    # edit menu ends

    
    # Help menu starts
    Helpmenu = Menu(Menubar , tearoff = 0)
    Helpmenu.add_command(label = "About",command=about)
    Menubar.add_cascade(label= "help",menu = Helpmenu)

    # Help menu ends

    root.config(menu = Menubar)

    # Adding scrollbar

    Scroll= Scrollbar(Textarea)
    Scroll.pack(side = RIGHT,fill=Y,ipadx = 2)
    Scroll.config(command = Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)


    root.mainloop()







