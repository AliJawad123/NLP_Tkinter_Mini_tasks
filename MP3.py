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


def getbai():
    pass



root=tk.Tk()
root.geometry("500x500")
root.configure(bg="orange")

#classes in tkinter
# bool, string ,int,double

#########  Background Image  ##############
 


###################################




Label1=tk.Label(root,text="Mood Tunes",fg="white",bg="blue",width=500,font="Times 25 bold italic")
Label1.pack()


Label2=tk.Label(root,text="Where words fail, music speaks.",fg="white",bg="purple",width=500,font="Times 14 bold italic",pady=20)
Label2.pack()


l2=tk.Label(root,text="Sentences ",bg="purple",font="Times 45 bold",fg="white")
l2.pack(pady=3)

l1=tk.Label(root) 
l1.pack()

############3333333333333333333333

# Load the image and create a PhotoImage object
image = Image.open("1.png")
photo = ImageTk.PhotoImage(image)

# Create a Label widget and set the image as its content
label5= tk.Label(root, image=photo)


resized_photo = photo.subsample(2)
label5.config(image=resized_photo)
label5.pack()




#################333333

l4=tk.Label(root,text="Words ",bg="purple",font="Times 20 bold",fg="white")
l4.pack(pady=3)

l3=tk.Label(root)
l3.pack()


b1=tk.Button(root,text="submit",command=getbai)
b1.pack()



root.mainloop()