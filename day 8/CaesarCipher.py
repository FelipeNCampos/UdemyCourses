

class App:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    logo = """           
        ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
        a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
        8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
        "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
        `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                    88             88                                 
                ""             88                                 
                                88                                 
        ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
        a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
        8b         88 88       d8 88       88 8PP""""""" 88          
        "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
        `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                    88                                             
                    88           
        """
    def __init__(self):
        answer = ""
        while (answer not in ['encode','decode']):
            answer = input("\n\nType 'encode' to encrypt or 'decode' to decrypt: ")
            if (answer not in ['encode','deconde']):
                print("Invalid option, choose again")
                continue
            break
            
        if (answer == "encode"):
            message = input("Type your menssage: ")
            shift = input("Type the shift number: ")

            result = self.encode(message,shift)

            print(f"Here's your encoded result : {result}")

        elif (answer == "decode"):
            message = input("Type your menssage: ")
            shift = input("Type the shift number: ")

            result = self.decode(message,shift)

            print(f"Here's your decoded result : {result}")
        again = input("Do you want go again ?(y or n)").lower()
        if (again == 'y'):
            self.__init__()




    def encode(self,text:str,shit:int) :
        result = ""
        for c in range(len(text)):
            index = self.alphabet.index(text[c])
            result += self.alphabet[index+int(shit)]

        return (result)
       
       
    def decode(self,text:str,shit:int):
        result = ""
        for c in range(len(text)):
            index = self.alphabet.index(text[c])
            result += self.alphabet[index-int(shit)]
        return result




Display  = App()
