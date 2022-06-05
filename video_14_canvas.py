
# line kheechne ke liye canvas widget ka use krenge

from tkinter import *

from matplotlib.pyplot import fill

root = Tk()


canvas_width = 800
canvas_height = 400


root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Aryan hai toh GUI hai")


can_widget = Canvas(root,width=canvas_width, height=canvas_height)

can_widget.pack()

# The line goes from the point x1 ,y2 to x2, y2

can_widget.create_line(0,0,800,200)

# creating rectangle with topleft cordinate and bottomright coordinate
can_widget.create_rectangle(3,5,700,300,fill="blue")
 
# creating a text 

can_widget.create_text(200,200,text ="Python")

# creating a oval --important--

can_widget.create_oval(344,233,244,355)















root.mainloop()