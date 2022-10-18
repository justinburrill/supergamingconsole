from tkinter import *
# Initialize window
root = Tk()

# Create canvas
winheight = 750
winwidth = 750
_canvas = Canvas(root, height=winheight, width=winwidth)
_canvas.pack()


# class Paddle():
#     def __init__(self, x):
#         self.length = 40
#         self.width = 10
#         self.xpos = x
#         self.ypos = winheight - self.width / 2


# paddle_dist_from_wall = 20
# player1 = Paddle(0 + paddle_dist_from_wall)
# player2 = Paddle(winwidth - paddle_dist_from_wall)
# paddles = [player1, player2]


# class Globe():
#     def __init__(self):
#         self.ballpos = []
#         self.ballW = 20

#     def reset(self):
#         self.ballpos = []


# globe = Globe()


# def rect(x, y, x2, y2, c):
#     _canvas.create_rectangle(
#         x, y, (x2), (y2), fill=c, outline=c)


# def draw():
#     # paddles
#     for p in paddles:
#         rect(p.xpos, p.ypos, p.xpos + p.width, p.length, "#000000")


# globe.reset()

# Needs to be here for tkinter
root.mainloop()
