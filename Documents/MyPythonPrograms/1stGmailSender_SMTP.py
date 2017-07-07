#Sending to mail
import smtplib
sender = "pkblanks2013@gmail.com"
receivers = ["pkblanks@yahoo.com"]

message = """From: Paa Kwesi <pkblanks2013@gmail.com>
To: Paa Kwesi <pkblanks@yahoo.com>
Subject: SMTP email test 

This is a test e-mail message.
"""

server = smtplib.SMTP('smtp.gmail.com', 587)	# this creates the SMTP server and host with port. 
server.ehlo() 									#this identifies you to the SMTP server
server.starttls()								#Put the SMTP connection in TLS (Transport Layer Security) mode
server.login("pkblanks2013@gmail.com", "type password") #Log in on the server
server.sendmail("pkblanks2013@gmail.com", "pkblanks@yahoo.com", message)         
server.quit()

print "Successfully sent email"



#to Unknown
# import smtplib
# sender = "pkblanks2013@gmail.com"
# receivers = ["abekuluiz@gmail.com"]

# message = """From: From Paa Kwesi <pkblanks2013@gmail.com>
# To: To Abeku <abekuluiz@gmail.com>
# Subject: SMTP email test 

# This is a test e-mail message.
# """

# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login("pkblanks2013@gmail.com", "typeemailpassword")
# message = "Hello Abeiku"
# smtpObj.sendmail("pkblanks2013@gmail.com", "abekuluiz@gmail.com", message)         
# smtpObj.quit()

# print "Successfully sent email"




