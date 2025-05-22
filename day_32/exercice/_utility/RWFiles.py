import json



class RWFiiler():


    @staticmethod
    def getJsonKey(path:str, dictKey):
        try:
            with open(path, "r") as f:
               return json.load(f)[0][dictKey]
        except:
            return "fail read sttpkey"
        
    @staticmethod
    def readJsonToDict(path:str):
        """
        giving path of a json, return a dict of this load json\n
        """
        try:
            with open(path, "r") as f:
                try:
                    return json.load(f)
                except:
                    raise IndexError("erro ao carregar o json")
        except:
            raise IndexError("erro ao abrir o json")
        
        