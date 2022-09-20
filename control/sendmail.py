# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_mail(user: str, passwordK: str):
    # create message object instance
    msg = MIMEMultipart()
    message = "Alerta sobre temperatura en regiones de:"
    # setup the parameters of the message
    password = passwordK
    msg['From'] = "admin@monitoreo"
    msg['To'] = user
    msg['Subject'] = "Alerta Temperatura"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()