from tkinter import *
from _Util.Util import Util
import random

class Gui(Tk):

    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Flashy")
        self.config(bg="lightgreen",padx=60,pady=30)
        self.minsize(width=600,height=500)
        self.start()

    def interface(self):
        self.lang = Label(text="Russo",font=(20))
        self.lang.grid(row=0,column=0,columnspan=3,sticky="nsew")

        
        self.kword = Button(text="palavra",width=25,height=10,font=("Arial",24),bg="lightyellow",command=self.flip)
        self.kword.grid(row=1,column=0,columnspan=3,rowspan=3,sticky="nsew")


        self.nobtn = Button(text="No",font=("arial",15),height=1,width=5,bg="red",fg="white")
        self.nobtn.grid(row=4,column=0,sticky="nsew")

        self.okbtn = Button(text="Yes",font=("arial bold",15),height=1,width=5,bg="green",fg="white")
        self.okbtn.grid(row=4,column=2,sticky="nsew")

    def newWord(self,data):
        self.choice = random.choice(data)
        self.kword.config(text=self.choice['ru'])
        




    def start(self):
        self.interface()
        data = Util.getDictWords()

        self.newWord(data)

        self.mainloop()


    def flip(self):
        if (self.lang.cget("text") == "Russo"):
            self.lang.config(text="Português")
            self.kword.config(text=self.choice['pt'],bg="lightblue")
        elif self.lang.cget("text") == "Português":
            self.lang.config(text="Russo")
            self.kword.config(text=self.choice['ru'],bg="lightyellow")

        Util.addPalavraConhecida()

teste = Gui()