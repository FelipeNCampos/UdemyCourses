

class app:
    logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    def __init__(self):
        save = {}
        print(self.logo)
        print("Welcome to the secret auction program.")

        ans = 'y'

        while ans == 'y':
            nome = input("What's your name?")
            bid = int(input("What's your bid? $"))

            save[nome] = bid

            ans = ""

            while ans not in['y','n']:
                ans = input("Are there any other bidders ? (y or n)").lower()
                if (ans not in ['y','n']):
                    print("Wrong answer, type again.")
                print("\n" * 100)
        print(f"Winner : {max(save, key=save.get)} with ${save[max(save, key=save.get)]} bid")

solution = app()