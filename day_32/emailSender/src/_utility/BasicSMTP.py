import smtplib
from src._utility.RWFiles import RWFiiler as rw

class BasicSMTP:
    
    def __init__(self,emailOwner,hostOwner):
        '''
        init with email and host defined 
        usage: 
        BasicSMTP("example@gmail.com","smtp.gmail.com")
        '''

        self.sender = emailOwner
        self.host = hostOwner
        self.connection = None
        self.port = 587

    def setEmail(self,email):
        '''
        CR(U)D of email

        ex:
        setHost("your.email.here")
        '''
        self.sender = email

    def setHost(self,host):
        '''
        CR(U)D of host

        ex:
        setHost("your.host.here")
        '''
        self.host = host

    def makeConnection(self):
        '''
        Make connection with host remind to close connection after used (closeConnection)

        need declared host,before makeConnection do:
        setHost("your.host.here")


        '''

        if self.host == "":
            raise ValueError("You need define email sender and host before")
        
        try:
            self.connection = smtplib.SMTP(self.host,port=self.port)
            self.connection.starttls()
        except:
            raise ValueError("Anything goes wrong while making connection ")

    def closeConnection(self):
        '''
        use for close smtp connection of this object
        '''
        self.connection.close()


    def login(self,user,password):
        '''
            login without app password
            ps: need connection first
        '''
        
        if not hasattr(self, 'connection') or self.connection is None:
            raise SyntaxError("You need connect before login")
        try:
            self.connection.login(user=user,password=password)
        except:
            raise ValueError("anything goes wrong while login")    

    def loginApp(self):
        '''
            login without app password
            ps: need connection and set sender first
        '''
        
        if not hasattr(self, 'connection') or self.connection is None:
            raise IndexError("You need connect before login")
        
        if self.sender == "":
            raise ValueError("You need set email user first.")
        try:
            password = rw.getSTTPkey()
            self.connection.login(user=self.sender,password=password)
        except:
            raise ValueError("anything goes wrong while login")        
        
    def mail(self, mailTo, message):
        '''
        Simple mail to,

        need:
        makeConneciton -> login
        before usage

        ex:
        mail("exemple@gmail.com", "Hello Word!")
        '''
        self.connection.sendmail(from_addr=self.sender,to_addrs=mailTo,msg=message)


    def sendMail(self, mailTo, message):
        '''
        Complet mail to using loginApp,


        ex:
        mail("exemple@gmail.com", "Hello Word!")
        '''
        self.makeConnection()
        self.loginApp()
        self.connection.sendmail(from_addr=self.sender,to_addrs=mailTo,msg=message)
        self.closeConnection()



