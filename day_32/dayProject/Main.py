from _utility.RWFiles import RWFiiler as rw
from smtp.doSMTP import DoSMTP
from datetime import datetime

class Main:

    def __init__(self):
        dt = datetime.now()
        self.do = DoSMTP("felipe.n.cmp@gmail.com", "smtp.gmail.com", rw.getJsonKey("config.json","smtpPass"))
        
        dados = rw.readJsonToDict("data/birthday.json")
        
        birdantes = []

        for x,y in dados[0].items():
            if y[0] == dt.day:
                if y[1] == dt.month:
                    birdantes.append([x,y[3]])

        for c in birdantes:
            print(c[1])
            print(self.do.sendMessage(c[1], f"anivesario desse buxa aqui -> {c[0]}", "Feliz dia Fela da P***"))

play = Main()