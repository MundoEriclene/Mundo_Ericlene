import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.maquina_relatorios import gerar_relatorio_sono  # Corrigida a importação
import os

# Configuração das variáveis a partir do Render
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")  # Deve ser configurado no Render
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Deve ser configurado no Render
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS", "").split(",")  # Deve ser configurado como lista separada por vírgula no Render

# Função para enviar e-mail
def enviar_email_relatorio():
    # Gerar o relatório
    relatorio = gerar_relatorio_sono()

    if not relatorio:
        print("❌ Falha ao gerar o relatório de sono.")
        return

    try:
        # Configurar o servidor SMTP
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        # Montar e enviar o e-mail para cada destinatário
        for destinatario in EMAIL_RECIPIENTS:
            mensagem = MIMEMultipart()
            mensagem["From"] = EMAIL_USER
            mensagem["To"] = destinatario.strip()
            mensagem["Subject"] = "Relatório de Saúde - Sono"

            corpo_email = MIMEText(relatorio, "plain")
            mensagem.attach(corpo_email)

            # Enviar o e-mail
            server.send_message(mensagem)
            print(f"✅ Relatório enviado com sucesso para {destinatario}")

    except smtplib.SMTPException as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

    finally:
        server.quit()

# Executar a função ao rodar o script
if __name__ == "__main__":
    enviar_email_relatorio()
