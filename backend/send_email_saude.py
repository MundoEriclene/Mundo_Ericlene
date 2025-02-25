import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from maquina_relatorios import gerar_assunto_relatorio, gerar_relatorio_sono

# ✅ Configurações de e-mail
GMAIL_USER = os.environ.get("GMAIL_USER", "mundoericlene@gmail.com")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD", "sua_senha_aqui")  # Configure no Render
DESTINATARIOS = os.environ.get("DESTINATARIOS", "email1@example.com,email2@example.com").split(',')

# 📤 Função para enviar e-mail
def enviar_relatorio_sono(dados_sono):
    try:
        # 🔍 Gerando relatório
        assunto = gerar_assunto_relatorio()
        corpo_relatorio = gerar_relatorio_sono(dados_sono)

        # 📧 Configurando a mensagem
        mensagem = MIMEMultipart()
        mensagem['From'] = GMAIL_USER
        mensagem['To'] = ", ".join(DESTINATARIOS)
        mensagem['Subject'] = assunto

        # 💬 Corpo do e-mail em HTML
        mensagem.attach(MIMEText(corpo_relatorio, 'plain'))

        # 🔒 Conexão segura com o servidor do Gmail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(GMAIL_USER, GMAIL_PASSWORD)
            servidor.sendmail(GMAIL_USER, DESTINATARIOS, mensagem.as_string())

        print("✅ E-mail enviado com sucesso para:", DESTINATARIOS)
        return {"status": "success", "message": "Relatório de sono enviado por e-mail com sucesso."}

    except smtplib.SMTPException as e:
        print("❌ Erro no envio do e-mail:", str(e))
        return {"status": "error", "message": "Erro ao enviar o e-mail."}

    except Exception as e:
        print("🚫 Erro inesperado:", str(e))
        return {"status": "error", "message": "Erro inesperado no envio de e-mail."}
