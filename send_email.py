from re import M
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email from python!"
sender_email = "thescientist952@gmail.com"
receiver_email = "prasathkannan2002@gmail.com"
password = input("Enter the password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>        
"""
message.add_alternative(html, subtype="html")
context =ssl.create_default_context()

print("Sending email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Sent")