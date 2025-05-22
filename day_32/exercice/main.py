import datetime as dt
from smtp.doSMTP import DoSMTP
from _utility.RWFiles import RWFiiler as rw
import random


class Main:

    def __init__(self):
        data = dt.datetime.now()
        self.do = DoSMTP("felipe.n.cmp@gmail.com","smtp.gmail.com", rw.getJsonKey("config.json","key"))

        message = "Hello World!"

        with open("frases.txt","r") as f:
            datadict = f.readlines()
            message = random.choice(datadict)

        if data.weekday() == 3:
            if not self.do.sendMessage("felipe_nunes@discente.ufg.br", message):
                   print("hit")


play = Main()