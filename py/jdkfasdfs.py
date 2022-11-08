from tkinter import *
import random
# Initialize window
root = Tk()

# Create canvas
WINRES = [1280, 1024]
winwidth = WINRES[0]
winheight = WINRES[1]
root.geometry(f"{winwidth}x{winheight}")
root.title("Test")

l = Label(root, text = "hi")
l.pack()
# Needs to be here for tkinter
root.mainloop()
