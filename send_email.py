import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(Recipient_email, Subject, Body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = Recipient_email
        msg['Subject'] = Subject

        msg.attach(MIMEText(Body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, Recipient_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending mail: {e}")

if __name__ == "__main__":
    recipient = "judesamuelo60@gmail.com"
    subject = "Email Test from Python"
    body = "This is a test email sent from you to you using python"
    send_email(recipient, subject, body)



