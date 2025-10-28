from tkinter import *

from PIL import Image, ImageTK

root= Tk()
root.title("image")
root.geometry("400*400")

upload= Image.open(wallpaper.jpg)
image= ImageTK.Photoimage(upload)

label= Label(root, image=image, height=300, width=400)
label.place(x=60, y=0)

root.mainloop()