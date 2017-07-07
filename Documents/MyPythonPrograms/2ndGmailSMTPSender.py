
#Importing modules 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#Composing basic headers 
print """
WELCOME TO PYTHON GMAIL SENDER"""

print '''
Kindly input the following Details'''
fromaddr = raw_input("Enter your address: ")
password = raw_input('Enter password: ')
toaddr = raw_input("Destination Email: ")
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = raw_input("Subject of Message: ")

#Attach body of the email to the MIME message:
body = raw_input("Type your message: ")
msg.attach(MIMEText(body, 'plain'))

#For sending the mail, we have to convert the object to a string, and 
#then use the same prodecure as above to send using the SMTP server.
print 'Connecting to server...'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, password)
print 'Preparing the email...'
print 'Disconnecting...'
text = msg.as_string()

print 'Sending...'
server.sendmail(fromaddr, toaddr, text)
print 'Done!'

print """
created by Paa Kwesi, 2017.
ALL RIGHTS RESERVED"""

		
