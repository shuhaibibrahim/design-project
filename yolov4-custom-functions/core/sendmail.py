import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#The mail addresses and password
sender_address = 'thirdeye1822@gmail.com'
sender_pass = 'thirdeye2021'
def sendmail(mail, number):
  receiver_address = mail
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = 'ODD EVEN SCHEME VIOLATION'   #The subject line
  mail_content=f"""Respected sir,
   
Your vehicle with registration number : {number} was found on roads disobeying odd even scheme... This is to inform you that you have been fined an amount of RS.1000 and should be paid within a time of 5 days from the day of receival of this email.
  
Thank you"""
  #The body and the attachments for the mail
  message.attach(MIMEText(mail_content, 'plain'))
  #Create SMTP session for sending the mail
  session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
  session.starttls() #enable security
  session.login(sender_address, sender_pass) #login with mail_id and password
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print('Mail Sent')
