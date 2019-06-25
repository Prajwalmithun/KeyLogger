'''Python script to send attachments with the help of yagmail '''
#working
import yagmail

class Attachmail:
    #constructor
    def __init__(self, myemail, passwd, reciever, sub, cont, filename):
        self.myemail = myemail
        self.passwd = passwd
        self.reciever = reciever
        self.filename = filename
        self.sub = sub
        self.cont = cont

    #function to send attachment
    def sendme(self):
        yag = yagmail.SMTP(self.myemail,self.passwd)
        yag.send(
            to= self.reciever,
            subject=self.sub,
            contents=self.cont,
            attachments=self.filename
        )