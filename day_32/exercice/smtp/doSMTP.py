import smtplib


class DoSMTP:

    def __init__(self, user:str, host:str, password:str, port:int = 587):
        """
        DoSMPT \n
        Usage:\n
            objName = DoSMTP("example@gmail.com","smtp.gmail.com")\n
        """

        self.user = user
        self.host = host
        self.password = password
        self.port = port


    def sendMessage(self, mailTo:str, message:str):
        """
        sendMessage usage: \n
        objDoSMTP.sendMessage("your16charpassword","target@gmail.com","Hello Word!")\n

        remind to set 2 auth onn for your account and create a app password\n

        code error:\n
        0 - ok\n
        1 - port and/or host invalid\n
        2 - user and/or password invalid\n
        3 - error in tls\n
        4 - error sending mail\n
        """

        try :
            with smtplib.SMTP(self.host, port=self.port) as conection:
                try:
                    conection.starttls()
                except:
                    return 3
                
                try :
                    conection.login(user=self.user, password=self.password)
                except:
                    return 2
                
                try:
                    finalMessage = f"From: felipe.n.cmp@gmail.com\nTo:{mailTo}\nSubject: Frase motivacional aleatoria'\n\n{message}"
                    conection.sendmail(from_addr=self.user, to_addrs=mailTo, msg=finalMessage )
                except:
                    return 4
                
        except:
            return 1
        
        return 0 