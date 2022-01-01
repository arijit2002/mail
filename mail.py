import smtplib
import getpass as g
from email.mime.text import MIMEText

body="""

Hey, 
This is sent from Python 
Thanks and regards
"""

msg=MIMEText(body)
fromAddr="__Sender's mailId__"
toAddr="__Receiver's mailId__"

msg['From']=fromAddr
msg['To']=toAddr
msg['Subject']="This is a test mail"

server=smtplib.SMTP("smtp.gmail.com",587) #587 is the gmail port number

#put the smtp connection in TLS mode
server.starttls()
server.login(fromAddr, '__Sender"s mail password__')
server.send_message(msg)
print("Mail sent")
server.quit()