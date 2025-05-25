from src.Gui import Gui
from _util.RandomQuestions import RQuestions

class main():

    def __init__(self):
        teste = RQuestions()
        teste.doRandom()
        self.gui = Gui()


main()