import requests
from _util.RW import RW


class RQuestions():

    def __init__(self):
        self.origin = "https://opentdb.com/api.php"
        
        self.rw = RW()



    def doRandom(self):

        try:
            response = requests.get(self.origin+"?amount=50&type=boolean")
            print(response)
            print(self.rw.saveQST("qst",response.json()))
        except:
            return "Err"


    def getQST(self,index):
        try:
            return self.rw.getData()['qst']["results"][index]


        except :

            return {"question":"","difficulty":"","correct_answer":"True"}


