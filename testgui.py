from tkinter import *

root = Tk() # put me at the top

# Make a label widget
myLabel1 = Label(root, text="test1")
myLabel2 = Label(root, text="test2 dsafsda")

# Pack it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)

root.mainloop()