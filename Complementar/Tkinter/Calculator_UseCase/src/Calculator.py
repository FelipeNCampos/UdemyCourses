from tkinter import *




class Calculator(Tk):




    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.valor = 0 
        self.operacao = ""
        self.title("Calculadora")
        self.minsize(width=325,height=320)

        self.resultado_var = StringVar()
        self.interface()
        self.mainloop()


    def interface(self):
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")
        display = Label(self, textvariable=self.resultado_var, font=("Arial", 24), anchor="e")

        btn_c = Button(self, text="C", command=self.limpar)
        btn_c.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
        btn_div = Button(self, text="/", command=lambda t="/", f=self.adicionar_operador: f(t))
        btn_div.grid(row=1, column=3,  sticky="nsew")

        botoes = [
            ("7", self.adicionar_numero), ("8", self.adicionar_numero), ("9", self.adicionar_numero), ("*", self.adicionar_operador),
            ("4", self.adicionar_numero), ("5", self.adicionar_numero), ("6", self.adicionar_numero), ("-", self.adicionar_operador),
            ("1", self.adicionar_numero), ("2", self.adicionar_numero), ("3", self.adicionar_numero), ("+", self.adicionar_operador),
            ("0", self.adicionar_numero),("-1",self.adicionar_numero), (".", self.adicionar_ponto), ("=", self.calcular),
        ]

        for i, (texto, funcao) in enumerate(botoes):
            btn = Button(self, text=texto, command=lambda t=texto, f=funcao: f(t))

            if texto=="0":
                btn.grid(row=2 + i // 4, column=i % 4, sticky="nsew",columnspan=2)
            elif texto!="-1":
                btn.grid(row=2 + i // 4, column=i % 4, sticky="nsew")


        for i in range(6):
            self.rowconfigure(i, weight=1)
        for j in range(4):
            self.columnconfigure(j, weight=1)

    def adicionar_numero(self, numero):
        self.operacao += numero
        self.resultado_var.set(self.operacao)

    def adicionar_operador(self, operador):
        if self.operacao and self.operacao[-1] not in "+-*/":
            self.operacao += operador
            self.resultado_var.set(self.operacao)

    def adicionar_ponto(self, ponto):
        if not self.operacao or self.operacao[-1] in "+-*/":
            self.operacao += "0."
        elif "." not in self.operacao.split()[-1]:
            self.operacao += ponto
        self.resultado_var.set(self.operacao)

    def calcular(self, _=None):
        try:
            resultado = eval(self.operacao)
            self.resultado_var.set(str(resultado))
            self.operacao = str(resultado)
        except:
            self.resultado_var.set("Erro")
            self.operacao = ""

    def limpar(self):
        self.operacao = ""
        self.resultado_var.set("")










