from tkinter import *
import random
import sys
sys.path.insert(0, '../util_package/')
from util_package import getres
# Initialize window
root = Tk()

# Create canvas
WINRES = getres.getres()
winwidth = WINRES[0]
winheight = WINRES[1]
root.geometry(f"{winwidth}x{winheight}")
root.title("Pong")

_canvas = Canvas(root, height=winheight, width=winwidth)
_canvas.configure(bg="#000000")
_canvas.pack()


class Ball():
    def __init__(self):
        self.xvel = 0
        self.yvel = 0
        self.size = 20
        self.reset()

    def randomVel(self):
        self.xvel = random.randrange(0, 10) / 10
        self.yvel = random.randrange(0, 10) / 10

    def update(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

    def reset(self):
        self.xpos = winwidth/2 - self.size/2
        self.ypos = winheight/2 - self.size/2

    def checkCollision(self):
        for p in paddles:
            if self.xpos + self.size > p.xpos or self.xpos - self.size < p.xpos + p.width:
                self.bounce()

    def bounce(self):
        print("BOUNCE!!")


ball = Ball()


class Paddle():
    def __init__(self, x):
        self.length = 150
        self.width = 15
        self.xpos = x
        self.reset()

    def reset(self):
        self.ypos = winheight/2 - self.length / 2


paddle_dist_from_wall = 20
player1 = Paddle(0 + paddle_dist_from_wall)
player2 = Paddle(winwidth - paddle_dist_from_wall - player1.width)
paddles = [player1, player2]


def inputDetected():
    print("input")
    if (globe.frozen):
        print("unfrozen")
        globe.frozen = False
        loop()


root.bind("<Up>", lambda event, : inputDetected())


def updateBall():
    print(ball.xpos, ball.ypos)


def rect(x, y, x2, y2, c):
    _canvas.create_rectangle(
        x, y, (x2), (y2), fill=c, outline=c)


def draw():
    rect(0, 0, winwidth, winheight, "#000000")
    # paddles
    for p in paddles:
        rect(p.xpos, p.ypos, p.xpos + p.width, p.ypos + p.length, "#ffffff")

    # ball
    rect(ball.xpos, ball.ypos, ball.xpos +
         ball.size, ball.ypos + ball.size, "#ffffff")

    # centre line
    rect(0, winheight/2, winwidth, winheight/2+1, "#e0e0e0")


def loop():
    if (globe.frozen):
        return
    print(loop)
    ball.update()

    draw()
    root.after(2000, loop())


class Globe():
    # def __init__(self):
    #     self.frozen = False

    def reset(self):
        self.frozen = True
        ball.reset()
        draw()
        root.after(500, ball.randomVel())


globe = Globe()

globe.reset()


# Needs to be here for tkinter
root.mainloop()
