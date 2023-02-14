# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 06:04:56 2023

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:50:17 2023

This is my new code for the sentence tokenizer

"""

import tkinter as tk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

###################################


def getbai():

    text=userentry.get()
    para=sent_tokenize(text)
    l1.config(text=para)
    

    
    
    
    # Break down the sentence into words
    words = text.split()
    
    # Display the words in the window
    for i in range(len(words)):
        name_list.append(((words[i]),i))
    l3.config(text=name_list)         
   
    
    

####################################
name_list=[]

root=tk.Tk()
root.geometry("500x500")

#classes in tkinter
# bool, string ,int,double

Label1=tk.Label(root,text="Enter your text here",fg="white",bg="purple",font="Times 20 italic")
Label1.pack()
userentry=tk.Entry(root,width=30,font="black 14")

userentry.pack(pady=3)


l2=tk.Label(root,text="Sentences ",bg="purple",font="Times 20 bold",fg="white")
l2.pack(pady=3)

lbx=tk.Listbox(root,width=50,height=50)
l1=tk.Label(lbx,fg="black",font="times 14 bold")
l1.pack()
lbx.pack()


l4=tk.Label(root,text="Words ",bg="purple",font="Times 20 bold",fg="white")
l4.pack(pady=3)

lbx1=tk.Listbox(root,width=50,height=50)
l3=tk.Label(lbx1)
l3.pack()
lbx1.pack()

b1=tk.Button(root,text="submit",command=getbai)
b1.pack(pady=50)



root.mainloop()

