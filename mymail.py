#working
#basic script

import smtplib

print("\nSending.......\n")
content = "github.com/Prajwalmithun/JobPortal.git"

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()

#start tls mode , after ehlo()
mail.starttls()


mail.login('tkushal216@gmail.com', 'yashpraj3498')
mail.sendmail('tkushal216@gmail.com', 'gbhatgoutham@gmail.com', content)

mail.close()

print("\nMessage sent!!\n")