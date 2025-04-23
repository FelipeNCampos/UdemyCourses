import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors \n"))

cchoose = random.randint(0,2)


if (choose == 0):
    print(rock)
    print("Computer choose:\n")
    if (cchoose == 0):
        print(rock)
        print("Draw")
        
    elif (cchoose == 1):
        print(paper)
        print("Game Over.")
        
    elif (cchoose == 2):
        print(scissors)
        print('You Win.')


elif (choose == 1):
    print(paper)
    print(f"Computer choose:\n{cchoose} ")

    if (cchoose == 0):
        print(rock)
        print('You Win.')
        
    elif (cchoose == 1):
        print(paper)
        print("Draw")
        
    elif (cchoose == 2):
        print(scissors)
        print("Game Over.")

elif (choose == 1):
    print(scissors)
    print(f"Computer choose:\n{cchoose} ")

    if (cchoose == 0):
        print(rock)
        print("Game Over.")
        
    elif (cchoose == 1):
        print(paper)
        print('You Win.')
        
    elif (cchoose == 2):
        print(scissors)
        print("Draw")
    