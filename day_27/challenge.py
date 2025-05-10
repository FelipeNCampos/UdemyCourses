from tkinter import *


def click():
    print("hit")


def clicked():
    print('yeah')

win = Tk()
win.title("challenge")
win.minsize(height=300,width=500)
win.config(padx=50,pady=50)

lbl = Label(text="Main label")
lbl.grid(column=0,row=0)


btn = Button(text="normal button",command=click)
btn.grid(row=1,column=1)


newbtn = Button(text="New button",command=clicked)
newbtn.grid(column=2,row=0)


ent = Entry()
ent.grid(row=2,column=3)

win.mainloop()
