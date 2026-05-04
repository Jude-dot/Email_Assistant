import imaplib
import email
import os
from dotenv import load_dotenv
load_dotenv()


imap_server = "imap.gmail.com"
email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, "ALL")
email_list = []
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])

    print(f"Message number is: {msgnum}")
    print(f"From: {message.get("From")}")
    print(f"To: {message.get("To")}")
    print(f"BCC: {message.get("BCC")}")
    print(f"Date: {message.get("Date")}")
    print(f"Subject: {message.get("Subject")}")

    print("Content:")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())

    email_list.append(message.get("From"))

imap.close()
print (email_list)




