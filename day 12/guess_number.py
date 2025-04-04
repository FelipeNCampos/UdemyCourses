import random



class GuessNumber:
    logo = r"""
     / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
    / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
   / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
   \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
    """


    def __init__(self):
        guesses  = 0
        print(self.logo)
        print("Welcome to the guess the number game\n I'm thinking of a number between 1 and 100")
        n = random.randint(1,100)

        dif = input("Choose the difficult:\n Easy('1') - Have 10 atempts to guess\n Hard('2') - Have 5 attempts to guess\n")
        while (dif not in ['1','2']):
            print("Invalid choise, choose again .")
            dif = input("Choose the difficult:\n Easy('1') - Have 10 atempts to guess\n Hard('2') - Have 5 attempts to guess\n")
        
        if (dif == '1'):
            guesses = 10
        else:
            guesses = 5

        for c in range(guesses):
            print(f"You have {guesses-c} attempts to guess the number ")
            g = int(input("Make a guess: "))
            if (g < n):
                print("^^^Too low^^^")
            elif (g > n):
                print("---Too high---")
            else:
                print(f"\n\n____________________You got it! The answer was {g}____________________\n\n")
                return 
        print(f"No more chances, you lose!\n The numer was {n}")



solution = GuessNumber()