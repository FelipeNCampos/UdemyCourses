import json



class RWFiiler():


    @staticmethod
    def getSTTPkey():
        try:
            with open("key.json", "r") as f:
               return json.load(f)[0]['key']
        except:
            return "fail read sttpkey"