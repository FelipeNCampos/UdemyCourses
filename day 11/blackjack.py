import random

class cassino:

    cards = []
    player = {'cards':[],'total':0}
    dealer = {'cards':[],'total':0}
    c_out = 0


    def mostrar(self,par):
        print("--------------------------------------------------")
        if (par):
            print(f"\n\nDealer cards : ", end="")
            for c in self.dealer['cards']:
                print(f"{c} ", end="")
            print(f"\nTOTAL : {self.dealer['total']}")

        else:    
            print(f"\n\nDealer cards : ", end="")
            print(f" {self.dealer['cards'][0]} *")
        
        print(f"\n\nPlayer cards : ", end="")
        for c in self.player['cards']:
            print(f"{c} ", end="")
        print(f"\nTOTAL : {self.player['total']}")


    def init(self):
        self.cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        player = {'cards':[],'total':0}
        dealer = {'cards':[],'total':0}
        c_out = 0

    def take_card(self,target):
        '''
        Dado jogador, retorna true se a jogada for possivel e false se resultar em Game Over. 
        '''
        num = 0
        temp = self.cards[random.randint(0,12 - self.c_out)]
        target['cards'].append(temp)

        if(temp in ['A','J','Q','K']):
            if (temp in ['A']):
                if (target['total'] + 11 > 21):
                    target['total'] += 1
                else:
                    target['total'] += 11
            else:
                target['total'] += 10
        else:
            target['total'] += int(temp)

        self.cards.remove(temp)
        self.c_out += 1

        if (target['total'] > 21):
            return True
        else:
            return False


    def play(self):
        self.init()

        for c in range(2):
            self.take_card(self.player)
            self.take_card(self.dealer)

        self.mostrar(0)

        ans = ""
        
        for c in range(5):
            while (ans not  in ['y','n']):
                ans = input("Hit ? (y or n )").lower()
            
            if (ans == 'y'):
                if (self.take_card(self.player)):
                    self.mostrar(1)
                    print('--------------------YOU LOSE--------------------')
                    return 
                else:
                    self.mostrar(0)
                ans = ''
            else:
                if (self.dealer['total'] <= self.player['total']):
                    if (self.take_card(self.dealer)):
                        self.mostrar(1)
                        print('--------------------YOU WIN--------------------')
                        return
                else:
                    self.mostrar(1)
                    print('--------------------YOU LOSE--------------------')


        
        
        


app = cassino()
app.play()
