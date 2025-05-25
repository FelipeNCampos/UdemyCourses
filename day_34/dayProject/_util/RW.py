import json




class RW():

    def __init__(self,origin = "./data/dataset.json"):
        self.origin = origin
    
    def readScore(self):
        

        try:
            with open(self.origin) as f:
                data = json.load(f)
                return data["score"]

        except FileNotFoundError:
            return 404
        
    def readMScore(self):
        

        try:
            with open(self.origin) as f:
                data = json.load(f)
                return data["maxscore"]

        except FileNotFoundError:
            return 404
        
    def saveMScore(self,value):

        try:
            with open(self.origin, "r") as f:
                data = (json.loads(f.read()))
            

            data["maxscore"] = value 


            with open(self.origin,"w") as f:
                json.dump(data,f,indent=4)
        
        except FileNotFoundError:
            return 404
        except :
            return 666
        
    def saveScore(self,value):

        try:
            with open(self.origin, "r") as f:
                data = (json.loads(f.read()))
            

            data["score"] = value 


            with open(self.origin,"w") as f:
                json.dump(data,f,indent=4)
        
        except FileNotFoundError:
            return 404
        except :
            return 666
    
    def saveQST(self,key,content):

        try:
            with open(self.origin, "r") as f:
                data = (json.loads(f.read()))
            

            data[key] = content


            with open(self.origin,"w") as f:
                json.dump(data,f,indent=4)
        
        except FileNotFoundError:
            return 404
        except :
            return 666
        
    def resetScore(self):

        try:
            with open(self.origin, "r") as f:
                data = (json.loads(f.read()))
            

            data["score"] = 0


            with open(self.origin,"w") as f:
                json.dump(data,f,indent=4)
        
        except FileNotFoundError:
            return 404
        except :
            return 666
        

    def getData(self):
        try:
            with open("./data/dataset.json") as f:
                data = json.loads(f.read())

                return data


        except FileNotFoundError:
            return 404


    def readLastQST(self):

        try:
            with open("./data/dataset.json") as f:
                data = json.loads(f.read())

                return data["last"]
            
        except FileNotFoundError:
            return 404
        
    def addLast(self,value):

        try:
            with open(self.origin, "r") as f:
                data = (json.loads(f.read()))
            

            data["last"] += value


            with open(self.origin,"w") as f:
                json.dump(data,f,indent=4)
        
        except FileNotFoundError:
            return 404
        except :
            return 666