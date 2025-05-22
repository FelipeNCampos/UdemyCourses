from src._utility.BasicSMTP import BasicSMTP 



class Main:
    
    def __init__(self):
        sm = BasicSMTP("felipe.n.cmp@gmail.com","smtp.gmail.com")
        sm.sendMail(mailTo="felipe_nunes@discente.ufg.br",message="teste de delay")


play = Main()