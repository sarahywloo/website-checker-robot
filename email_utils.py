import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv 

load_dotenv(override=True)

def send_email_alert(subject, body):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("mail.dentalopolis.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())

    except Exception as e:
        print(f"Failed to send email: {e}")