from tkinter import *
from classes.utility.Util import Util
import random

class Gui(Tk):

    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Flashy")
        self.config(bg="lightgreen",padx=60,pady=30)
        self.minsize(width=600,height=500)
        self.start()

    def start(self):
        self.interface()
        self.data = Util.getDictWords()

        self.newWord()

        self.mainloop()


    def interface(self):
        self.lang = Label(text="Russo",font=(20))
        self.lang.grid(row=0,column=0,columnspan=3,sticky="nsew")

        
        self.kword = Button(text="palavra",width=25,height=10,font=("Arial",24),bg="lightyellow",command=self.flip)
        self.kword.grid(row=1,column=0,columnspan=3,rowspan=3,sticky="nsew")


        self.nobtn = Button(text="No",font=("arial",15),height=1,width=5,bg="red",fg="white", command=self.noButton)
        self.nobtn.grid(row=4,column=0,sticky="nsew")

        self.okbtn = Button(text="Yes",font=("arial bold",15),height=1,width=5,bg="green",fg="white",command=self.yesButton)
        self.okbtn.grid(row=4,column=2,sticky="nsew")

    def newWord(self):
        self.choice = random.choice(self.data)
        know = Util.readKnow()

        while self.choice in know:
            self.choice = random.choice(self.data)

        self.kword.config(text=self.choice['ru'], bg="lightyellow")
        self.lang.config(text="Russo")
        


    def flip(self):
        if (self.lang.cget("text") == "Russo"):
            self.lang.config(text="Português")
            self.kword.config(text=self.choice['pt'],bg="lightblue")
        elif self.lang.cget("text") == "Português":
            self.lang.config(text="Russo")
            self.kword.config(text=self.choice['ru'],bg="lightyellow")

    def yesButton(self):
        Util.addPalavraConhecida(self.choice)
        self.newWord()


    def noButton(self):
        self.newWord()

