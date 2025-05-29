from tkinter import *
from _util.RW import RW
import html
from _util.RandomQuestions import RQuestions

class Gui(Tk):

    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.rw = RW()
        self.rq = RQuestions()

        self.vscore = self.rw.readScore()

        self.minsize(width=350,height=450)
        self.config(bg="gray95",padx=20,pady=20)

        self.last = self.rw.readLastQST()

        self.score = self.rw.readScore()

        self.qst = self.rq.getQST(self.last)

        self.interface()
        self.mainloop()
        

    def interface(self):
        self.label = Label(text=html.unescape(self.qst["question"]),width=30,height=15,font=("Verdana",12),bg="gray80",wraplength=300,anchor="n",pady=30)
        self.label.grid(row=1,column=0,rowspan=2,columnspan=3)


        self.score = Label(text="Score: "+str(self.vscore)+"|Max: "+str(self.rw.readMScore()),width=15,font=("Verdana",10),anchor="nw")
        self.score.grid(row=0,column=2)

        self.dif = Label(text="Dificulty: "+self.qst["difficulty"],width=15,font=("Verdana",9),anchor="nw")
        self.dif.grid(row=0,column=0)

        self.yesBTN = Button(text="✔",font=("Verdana",16),command=lambda f = self.check,p=1:f(p))
        self.yesBTN.grid(row=3,column=0)

        self.noBTN = Button(text="❌",font=("Verdana",16),command=lambda f = self.check,p=0:f(p))
        self.noBTN.grid(row=3,column=2)

    

    def check(self,ans):
        if ans == 1:
            if self.qst["correct_answer"]=="True":
                self.hitScore()
                self.after(1000,lambda f=self.nextqst : f())
                
            else:
                self.lostScore()
                self.after(1000,lambda f=self.nextqst : f())


        if ans==0 :
            if self.qst["correct_answer"]=="False":
                self.hitScore()
                self.after(1000,lambda f=self.nextqst : f())
            else:
                self.lostScore()
                self.after(1000,lambda f=self.nextqst : f())




    def nextqst(self):
        if self.last+1 == 50:
            self.rq.doRandom()
            self.last = -1
            self.rw.addLast(-50)

        self.last +=1
        self.rw.addLast(1)

        self.dif.config(text="Dificulty: "+self.qst["difficulty"])
        self.score.config(text="Score: "+str(self.vscore)+"|Max: "+str(self.rw.readMScore()))

        self.qst = self.rq.getQST(self.last)

        self.label.config(text=html.unescape(self.qst["question"]))

    def hitScore(self):
        self.after(1000,self.lgray)
        self.vscore += 1

        self.score.config(text="Score: "+str(self.vscore)+"|Max: "+str(self.rw.readMScore()))

        self.rw.saveScore(self.vscore)
        self.label.config(bg="green")


    def lostScore(self):
        self.after(1000,self.lgray)
        temp = int(self.rw.readMScore())
        if temp < int( self.vscore):
            self.rw.saveMScore(int(self.vscore))

        self.vscore = 0
        self.score.config(text="Score: "+str(self.vscore)+"|Max: "+str(self.rw.readMScore()))
        self.rw.resetScore()
        self.label.config(bg="red")

    def lgray(self):
        self.label.config(bg="gray80")