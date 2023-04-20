import smtplib 
from email.message import EmailMessage

# Creating a object for EmailMessage
email = EmailMessage() 
email['from'] = 'sender id'
email['to'] = 'receiver id'
email['subject'] = 'subject'  # Subject of email
email.set_content("content of email") # content of email

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:     
## sending request to server 
    
    smtp.ehlo()          # server object
    smtp.starttls()      # send data between server and client
    smtp.login("email_id", "Password") # login id and password of gmail
    smtp.send_message(email)   # Sending email
    print("email sent successfully")    # success message
