# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 00:20:34 2023

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from PIL import Image, ImageTk
import pygame

def play(song):
    

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    

def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()
    

    


root=tk.Tk()
root.geometry("900x500")
root.configure(bg="black")
root.title("Desktop MP3")
root.iconbitmap("icon.ico")



#classes in tkinter
# bool, string ,int,double

#########  Background Image  ##############

photos=[]




Label1=tk.Label(root,text="Mood Tunes",fg="black",bg="pink",width=30,font="Helvetica 25 bold italic")
Label1.pack(pady=3)


Label2=tk.Label(root,text="Where words fail, music speaks.",fg="white",bg="black",width=30,font="Times 14 bold italic",pady=20)
Label2.pack()


##########################

image = Image.open("6.png")
image1 = Image.open("5.png")
image2= Image.open("3.png")
image3= Image.open("4.png")

image = image.resize((200, 200), Image.ANTIALIAS)
image1=image1.resize((200, 200), Image.ANTIALIAS)
image2=image2.resize((200, 200), Image.ANTIALIAS)
image3=image3.resize((200, 200), Image.ANTIALIAS)

photos.append(ImageTk.PhotoImage(image))
photos.append(ImageTk.PhotoImage(image1))
photos.append(ImageTk.PhotoImage(image2))
photos.append(ImageTk.PhotoImage(image3))



f1 =tk.Frame(root, width=400, height=200, pady=14,bg="pink")

l2=tk.Label(f1,text="Kahani 2.0  ",bg="black",font="Times 20 bold",fg="white",padx=10,pady=10)
l2.pack(pady=2)

l9=tk.Label(f1, image=photos[2], anchor="e").pack()

b1=tk.Button(f1,text="Play",padx=15,command=lambda: play("Kahani-Suno-2.0(PaglaSongs).mp3"))
b1.pack(side=tk.LEFT)


b2=tk.Button(f1,text="Pause",command=pause,padx=15)
b2.pack(side=tk.LEFT)

b3=tk.Button(f1,text="Unpause",command=unpause,padx=15)
b3.pack(side=tk.LEFT)

f1.pack(side=tk.LEFT,pady=0,padx=10)


#########################

f2 =tk.Frame(root, width=400, height=200, pady=14,bg="pink")

l11=tk.Label(f2,text="Bol-hu",bg="black",font="Times 20 bold",fg="white",padx=10,pady=10)
l11.pack(pady=2)

l10=tk.Label(f2, image=photos[1], anchor="e").pack()


bb1=tk.Button(f2,text="Play",padx=15,command=lambda: play("bol-hu.mp3"))
#bb1=tk.Button(f2,text="Play",command=play,padx=15)
bb1.pack(side=tk.LEFT)


bb2=tk.Button(f2,text="Pause",command=pause,padx=15)
bb2.pack(side=tk.LEFT)

bb3=tk.Button(f2,text="Unpause",command=unpause,padx=15)
bb3.pack(side=tk.LEFT)

#f2.pack(padx=5,pady=35)
f2.pack(side=tk.LEFT)

############3333333333333333333333

f3 =tk.Frame(root, width=400, height=200, pady=14,bg="pink")

l111=tk.Label(f3,text="Barishein",bg="black",font="Times 20 bold",fg="white",padx=10,pady=10)
l111.pack(pady=2)

l110=tk.Label(f3, image=photos[0], anchor="e").pack()


bb11=tk.Button(f3,text="Play",padx=15,command=lambda: play("Baarishein(PaglaSongs).mp3"))
#bb1=tk.Button(f2,text="Play",command=play,padx=15)
bb11.pack(side=tk.LEFT)


bb12=tk.Button(f3,text="Pause",command=pause,padx=15)
bb12.pack(side=tk.LEFT)

bb13=tk.Button(f3,text="Unpause",command=unpause,padx=15)
bb13.pack(side=tk.LEFT)

f3.pack(side=tk.LEFT,padx=4)



#################333333

f9 =tk.Frame(root, width=400, height=200, pady=14,bg="pink")

llll2=tk.Label(f9,text="Rim-Jhim ",bg="black",font="Times 20 bold",fg="white",padx=10,pady=10)
llll2.pack(pady=2)

llll9=tk.Label(f9, image=photos[3], anchor="e").pack()

b1lll=tk.Button(f9,text="Play",padx=15,command=lambda: play("Rim-Jhim-Yeh-Sawan(PaglaSongs).mp3"))
b1lll.pack(side=tk.LEFT)


b2lll=tk.Button(f9,text="Pause",command=pause,padx=15)
b2lll.pack(side=tk.LEFT)

blll3=tk.Button(f9,text="Unpause",command=unpause,padx=15)
blll3.pack(side=tk.LEFT)

f9.pack(side=tk.LEFT,pady=0,padx=10)




root.mainloop()
