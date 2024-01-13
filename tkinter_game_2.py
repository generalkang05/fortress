from tkinter import *
from datetime import datetime

win = Tk()
win.title("GAME")
win.geometry("500x500")

cvs = Canvas(win)
cvs.config(width=500, height=500, bd=0, highlightthickness=0)



cvs.pack()

win.update()

t_0 = datetime.now()
while True:
    
    win.update()
