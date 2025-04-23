import art
import time 

class CoffeMachine:

    coffe = 0
    milk = 0
    water = 0


    def __init__(self):
        coffe = int(input("Coffe input: "))
        milk = int(input("Milk input: "))
        water = int(input("Water input: "))

        self.coffe = coffe
        self.milk = milk
        self.water = water

    def report(self):
        print(f"\n\n{"------Report------":^50} \n")    
        print(f"  Coffe : {self.coffe}")    
        print(f"  Milk : {self.milk}")    
        print(f"  Water : {self.water}\n\n")    

    def comprar(self,option,money):
        if (option == 1):
            if (self.coffe < 18):
                print(f"{"Lamento, caffe insuficiênte.":^50}")
                return False
            
            if (self.water < 50):
                print(f"{"Lamento, água insuficiênte.":^50}")
                return False
            if (money < 1.5):
                print(f"{"Lamento, dinheiro insuficiênte":^50}")
                return False
            
            self.coffe -= 18
            self.water -= 50
            troco  = money - 1.5


            print(f"{"------Compra realizada------":^50}\n pegue seu troco : ${troco} \n{art.cafe}")
            return True

        elif (option == 2):
            if (self.coffe < 24):
                print(f"{"Lamento, cafe insuvficiênte":^50}")
                return False
            
            if (self.milk < 150):
                print(f"{"Lamento, leite insuficiênte.":^50}")
                return False
            
            if (self.water < 200):
                print(f"{"Lamento, água insuficiênte.":^50}")
                return False
            
            if (money < 2.5):
                print(f"{"Lamento, dinheiro insuficiênte":^50}")
                return False

            self.coffe -= 24
            self.milk -= 150
            self.water -= 200
            troco  = money - 2.5



            print(f"{"------Compra realizada------":^50}\n pegue seu troco : ${troco:.2} \n{art.cafe}")

            return True
        
        elif (option == 3):
            if (self.coffe < 24):
                print(f"{"Lamento, cafe insuvficiênte":^50}")
                return False
            
            if (self.milk < 100):
                print(f"{"Lamento, leite insuficiênte.":^50}")
                return False
            
            if (self.water < 250):
                print(f"{"Lamento, água insuficiênte.":^50}")
                return False
            
            if (money < 3):
                print(f"{"Lamento, dinheiro insuficiênte":^50}")
                return False

            self.coffe -= 24
            self.milk -= 100
            self.water -= 250
            troco  = money - 3



            print(f"{"------Compra realizada------":^50}\n pegue seu troco : ${troco:.2} \n{art.cafe}")

            return True
        else:
            print(f"\n\n{"Opção invalida de compra":^50}")
            return False



    def receber(self):
        penny = int(input("\n\nQuantos Penny foram entregues :  "))
        nickel = int(input("Quantos nickel foram entregues :  "))
        dime = int(input("Quantos dime foram entregues :  "))
        quarter = int(input("Quantos quarter foram entregues :  "))
        
        return (penny*0.01)+(nickel*0.05)+(dime*0.10)+(quarter*0.25)

    def operation(self):
        time.sleep(3)
        print("\n"*200+"Bem vindo a maquina de cafe ")
        print(art.logo)
        choose = input("Menu :\n\n1 - Expresso ($1,5)\n2 - Latte ($2,5)\n3 - Cappuccino ($3,0)\n\nQual sua preferêcnia ? ").lower()
        if (choose == "report"):
            self.report()
            return
        
        elif (choose == "1"):
            dinheiro = self.receber()
            self.comprar(1,dinheiro)
        elif (choose == "2"):
            dinheiro = self.receber()
            self.comprar(2,dinheiro)
        elif (choose == "3"):
            dinheiro = self.receber()
            self.comprar(3,dinheiro)
        else:
            print("Opção inválida, escolha novamente.")
        



solution = CoffeMachine()
while 1:
    solution.operation()