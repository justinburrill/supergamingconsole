# justin burrill 14 10 22

from tkinter import *
from os import listdir


root = Tk() # put me at the top

MONITOR_RES = "1600x900" # i don't know if this is right
root.geometry(MONITOR_RES)

path = "./py" # dir to look for games

game_list = [f for f in listdir(path)] # get list of games

for game in game_list:
    game_name = Label(root, text=game)
    game_name.pack()
    img = PhotoImage(file=f"ico/{game}.png")
    canvas = Canvas(root, width = 300, height = 300)
    canvas.pack()
    canvas.create_image(20,20, anchor=NW, image=img)







root.mainloop()