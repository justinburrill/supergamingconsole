from tkinter import *

root = Tk() # put me at the top

def click():
    myLabel = Label(root, text="hey")
    myLabel.pack()

button = Button(root, text="button", command=click, padx=20)

button.pack()



root.mainloop()