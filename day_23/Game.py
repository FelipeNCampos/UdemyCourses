from turtle import Screen
from Player import Player
from Carro import Carro
import time 
import threading 



class Game:
    _status = 1
    _player = Player()
    def __init__(self):
        self.screen = Screen()
        self.screen.listen()
        self.screen.title("Tutle crossing")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        
        self.screen.onkeypress(self._player.move_up,"w")
        self.screen.onkeypress(self._player.move_down,"s")

        
        thread_spawn = threading.Thread(target=Carro.create_car)
        thread_via = threading.Thread(target=Carro.move_cars)
        thread_contato = threading.Thread(target=Game.contato)

        thread_via.start()
        thread_spawn.start()
        thread_contato.start()

        self.screen.mainloop()

    def contato():
        while True:
            for c in Carro._carros:
                if (Game._player.distance(c) < 20):
                    print("bateu")
                    Game._status = 0

    

play = Game()