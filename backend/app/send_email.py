import smtplib
from email.mime.text import MIMEText
import os

def enviar_email(destinatarios, assunto, mensagem):
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    
    msg = MIMEText(mensagem)
    msg["Subject"] = assunto
    msg["From"] = email_user
    msg["To"] = ", ".join(destinatarios)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email_user, email_password)
        server.sendmail(email_user, destinatarios, msg.as_string())
