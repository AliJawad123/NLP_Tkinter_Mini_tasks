# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:39:45 2023

@author: HP
"""

import pandas as pd
df=pd.read_csv('spam.csv', encoding='ISO-8859-1')
df = df.iloc[:, 0:2]
df

df['spam'] = df['Category'].apply(lambda x: 1 if x =='spam' else 0)


from sklearn.model_selection import train_test_split


# Here the message is the X and spam is Y

X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

from sklearn.feature_extraction.text import CountVectorizer

v = CountVectorizer()


# Here inside the transform when we supply the x train it will generate the BOW for the X train

X_train_cv = v.fit_transform(X_train.values)
X_train_cv

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train_cv, y_train)

X_test_cv = v.transform(X_test)

y_pred = model.predict(X_test_cv) 
y_pred

emails = [
    'Hey mohan, can we get together to watch footbal game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
]

new_e=v.transform(emails)

y_pred = model.predict(new_e)

print(y_pred)


def getbai():
    u1=userentry.get()
    name_list.append(u1)
    new_e=v.transform(name_list)
    y_pred = model.predict(new_e)
    store=""
    if y_pred[0]==0:
        store="Not Spam"
    elif y_pred[0]==1:
        store="Spam"


    l1.config(text=store)
    
name_list=[]
#########################################################
#              CODE FOR GUI                             #
#########################################################
import tkinter as tk

root=tk.Tk()
root.geometry("500x500")

Label1=tk.Label(root,text="Enter your text here",fg="white",bg="purple",font="Times 24 italic")
Label1.pack()
userentry=tk.Entry(root,width=30)

userentry.pack(pady=3)


l2=tk.Label(root,text="This email is classified as ",bg="purple",font="Times 20 bold",fg="white")
l2.pack(pady=3)

l1=tk.Label(root)
l1.pack()

b1=tk.Button(root,text="submit",command=getbai)
b1.pack()








root.mainloop()










