import random 



words = ["aardvark", "baboon", "camel"]
lifes = 6
wrong = []

stages = stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

key = words[random.randint(1,2)]
game = ""
for c in range(len(key)):
    game += "_"


while (lifes > 0 and "_" in game):
    print(stages[lifes])

    print(f"\nYour word is {game}")

    print("\nWorng guesses: ", end="")

    
    for c in wrong:
        print(f' "{c}" ',end="")
    print("\n")

    guess = input("guess a letter : ").lower()[0]

    if (guess in key):
        print("Hit \n")
        for c in range(len(key)):
            if guess == key[c]:
                game = game[:c] + guess + game[c + 1 :]
    else:
        print("Wrong , -1 life")
        lifes -= 1
        wrong.append(guess)

if (lifes > 0):
    print(stages[lifes])
    print("----------------------Win-----------------------")

else :
    print("\n Right word : "+key)
    print(stages[lifes])
    print ("___________________________Loose____________________________")