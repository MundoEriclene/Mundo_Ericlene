import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from backend.app.saude import gerar_relatorio_sono  # Função que gera o relatório de sono
import os

# Configuração das variáveis a partir do Render
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = os.getenv("mundoericlene@gmail.com")
EMAIL_PASSWORD = os.getenv("qffrtpickskghfgm")
EMAIL_RECIPIENTS = os.getenv("ericlenedesousa@gmail.com,ericlenes6@gmail.com").split(",")  # Lista de destinatários separados por vírgula

# Função para enviar e-mail
def enviar_email_relatorio():
    # Gerar o relatório
    relatorio = gerar_relatorio_sono()

    # Configurar o servidor SMTP
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)

    # Montar o e-mail
    for destinatario in EMAIL_RECIPIENTS:
        mensagem = MIMEMultipart()
        mensagem["From"] = EMAIL_USER
        mensagem["To"] = destinatario.strip()
        mensagem["Subject"] = "Relatório de Saúde - Sono"

        corpo_email = MIMEText(relatorio, "plain")
        mensagem.attach(corpo_email)

        # Enviar o e-mail
        server.send_message(mensagem)
        print(f"Relatório enviado para {destinatario}")

    server.quit()

# Executar a função ao rodar o script
if __name__ == "__main__":
    enviar_email_relatorio()
