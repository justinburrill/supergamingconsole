from tkinter import *
# Initialize window
root = Tk()

class Globe():
    def __init__(self):
        self.paddle1 = []
        self.paddle2 = []
        self.ball = []
        self.ballW = 20
    def reset(self):
        self.paddle1 = []
        self.paddle2 = []
        self.ball = []

globe = Globe()

# Create canvas
_canvas = Canvas(root, height=750, width=750)
_canvas.pack()

def rect(x, y, x2, y2, c):
    _canvas.create_rectangle(
                    x, y, (x2), (y2), fill=c, outline=c)

# def draw:
#     if 


globe.reset()

# Needs to be here for tkinter
root.mainloop()