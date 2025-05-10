from tkinter import *

def calcula():
    if ent.get() == '':
        valor = 0
    else:
        valor = float(ent.get())

    res = round(valor *1.609,2)

    
    lblres.config(text=res)


win = Tk()
win.minsize(width=150,height=100)
win.title("Miles to Km")
win.config(padx=30,pady=30)


ent = Entry()
ent.grid(row=0,column=1)
ent.config(width=15)


lblmiles = Label(text="Miles")   
lblmiles.grid(row=0,column=2)

lblis = Label(text="is equal to")
lblis.grid(row=1,column=0)

lblres = Label(text="0")
lblres.grid(row=1,column=1)


lblkm = Label(text="Km")
lblkm.grid(row=1,column=2)


btn = Button(text='Calculate', command=calcula)
btn.grid(row=2,column=1)


win.mainloop()