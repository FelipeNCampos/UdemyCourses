from tkinter import * 


class Ui(Tk):

    def interface(self):
        teste = Label(width=10)
        teste.grid(row=0,column=0)

        self.title = Label(text="Flash Card")
        self.title.grid(row=0,column=2)

        self.card = Button(text="Word",width=50,height=10)
        self.card.grid(row=1,column=1,rowspan=3,columnspan=3)

        self.btn_yes = Button(text="yes",width=10)
        self.btn_yes.grid(row=3,column=2)
        
        self.btn_no = Button(text="no",width=10)
        self.btn_no.grid(row=3,column=1)
        
    def __init__(self):
        super().__init__()
        self.minsize(width=500,height=300)
        self.config(padx=10,pady=20,background="Green")
        self.interface()
        
    
