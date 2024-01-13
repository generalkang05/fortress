from tkinter import *
from PIL import Image, ImageTk
win = Tk()
win.geometry("500x500")
win.title("Game")

cvs = Canvas(win)
cvs.config(width=500, height=500, bd=0, highlightthickness=0)
p1 = (250, 250)
# cvs.create_text(p1, text="GAME", font = ("Trial", 50), fill = "mazenta")

img = Image.open("./img/tank.png")
img = img.resize((50, 50))
img = img.rotate(0)
img = ImageTk.PhotoImage(img, master = win)
cvs.create_image(p1, image=img)

cvs.pack()

win.mainloop()