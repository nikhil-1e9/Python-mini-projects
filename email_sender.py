import smtplib

# list of email_ids to send the mail to
emails = ["random@gmail.com", "your.email@gmail.com"]

for email in emails:
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("sender_email_id", "sender_email_id_password")
	message = "Message_you_need_to_send"
	s.sendmail("sender_email_id", email, message)
	s.quit()
	
