from http.client import ImproperConnectionState
from tkinter import *

root = Tk()

root.geometry("644x244")

root.title("Code with harry- Title of my gui")

root.wm_iconbitmap("gui.png")

root.configure(background="grey")

widht = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{widht}x{height}")

Button(text = "close",command=root.destroy).pack()





root.mainloop()