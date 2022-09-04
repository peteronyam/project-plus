from email.message import EmailMessage
from email_sender import password


sender = "peteronyam@gmail.com"
password = password
import ssl
import smtplib


email_reciever = 'drillmonk@gmail.com'

head = "improve yourself"
body = """
welcome to python, you will do great things
"""

em = EmailMessage
em['From'] = sender
em['To'] = email_reciever
em['head'] = head
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, email_reciever, em.as_string())