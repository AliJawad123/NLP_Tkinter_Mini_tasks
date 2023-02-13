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
   
    
    """
    name_list.append(u1)
    print(name_list)
    text=str(name_list)

    real=sentence_tokenizer(text)
    words=str(word_tokenize(real))
    print(words)


    l1.config(text=real)
    l3.config(text=words)
    """


####################################
name_list=[]

root=tk.Tk()
root.geometry("500x500")

#classes in tkinter
# bool, string ,int,double

Label1=tk.Label(root,text="Enter your text here",fg="white",bg="purple",font="Times 15 italic")
Label1.pack()
userentry=tk.Entry(root,width=30)

userentry.pack(pady=3)

l2=tk.Label(root,text="Sentences ",bg="purple",font="Times 20 bold",fg="white")
l2.pack(pady=3)

l1=tk.Label(root)
l1.pack()


l4=tk.Label(root,text="Words ",bg="purple",font="Times 20 bold",fg="white")
l4.pack(pady=3)

l3=tk.Label(root)
l3.pack()


b1=tk.Button(root,text="submit",command=getbai)
b1.pack()



root.mainloop()

