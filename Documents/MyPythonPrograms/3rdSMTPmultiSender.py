
#Importing modules 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Composing basic headers 
print """
HELLO, WELCOME TO PYTHON MAIL SENDER!!!"""
name = raw_input("What is your name? ")
print "welcome " +name, "Enjoy Using!!"

print "Kindly input the following Details" 

print("select your account type")
print("1.Gmail")
print("2.Hotmail")
print("3.YahooMail")
print("4.Others")

#For sending the mail, we have to convert the object to a string, and 
#then use the same prodecure as above to send using the SMTP server.
print 'Connecting to server...'

account_type = raw_input("Enter Choice (1/2/3/4): ")
if account_type == "1":
	print "Gmail Account Details"
	fromaddr = raw_input("Enter your address: ")
	password = raw_input('Enter password: ')
	toaddr = raw_input("Destination Email: ")
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = raw_input("Subject of Message: ")

	#Attach body of the email to the MIME message:
	body = raw_input("""Type your message: 
	""")
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
	created by Paa Kwesi
	  credit: sumohammed
		ALL RIGHTS RESERVED
		2017"""

elif account_type == "2":
	print "Hotmail Account Details"
	fromaddr = raw_input("Enter your address: ")
	password = raw_input('Enter password: ')
	toaddr = raw_input("Destination Email: ")
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = raw_input("Subject of Message: ")

	#Attach body of the email to the MIME message:
	body = raw_input("""Type your message: 
	""")
	msg.attach(MIMEText(body, 'plain'))

	#For sending the mail, we have to convert the object to a string, and 
	#then use the same prodecure as above to send using the SMTP server.
	print 'Connecting to server...'
	server = smtplib.SMTP('smtp.live.com', 25)
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
	created by Paa Kwesi
	  credit: sumohammed
		ALL RIGHTS RESERVED
		2017"""

elif account_type == "3":
	print "Yahoo Account Details"
	fromaddr = raw_input("Enter your address: ")
	password = raw_input('Enter password: ')
	toaddr = raw_input("Destination Email: ")
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = raw_input("""Subject of Message:
	""")

	#Attach body of the email to the MIME message:
	body = raw_input("Type your message: ")
	msg.attach(MIMEText(body, 'plain'))

	#For sending the mail, we have to convert the object to a string, and 
	#then use the same prodecure as above to send using the SMTP server.
	print 'Connecting to server...'
	server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
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
	created by Paa Kwesi
	  credit: sumohammed
		ALL RIGHTS RESERVED
		2017"""

else:
	print """Account Type Unavailable/ under construction
		Try in some few days time"""


	print """
	created by Paa Kwesi
	  credit: sumohammed
		ALL RIGHTS RESERVED
			2017"""

