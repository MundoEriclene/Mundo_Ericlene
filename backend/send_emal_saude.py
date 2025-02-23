import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai

# Configurar as credenciais usando variáveis de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")
remetente = os.getenv("EMAIL_USER")
senha = os.getenv("EMAIL_PASSWORD")

if not remetente or not senha:
    raise ValueError("❌ Credenciais de e-mail não configuradas corretamente. Verifique suas variáveis de ambiente.")

# Gerar resposta usando a OpenAI
def gerar_resposta_openai(mensagem):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em saúde e bem-estar."},
                {"role": "user", "content": mensagem}
            ]
        )
        resposta_texto = resposta.choices[0].message.content.strip()
        return resposta_texto
    except Exception as e:
        print(f"❌ Erro ao conectar com a OpenAI: {e}")
        return None

# Função de envio de e-mail
def enviar_email_relatorio(destinatario, assunto, mensagem):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(remetente, senha)
            server.send_message(msg)
            print("✅ E-mail enviado com sucesso!")
    except smtplib.SMTPAuthenticationError:
        print("❌ Erro de autenticação. Verifique e-mail e senha.")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

# Função de envio automático ao salvar dados de sono
def enviar_relatorio_automatico(destinatario, prompt):
    resposta = gerar_resposta_openai(prompt)
    if resposta:
        assunto = "📊 Relatório Automático de Saúde"
        corpo = f"Aqui está sua análise de saúde:\n\n{resposta}"
        enviar_email_relatorio(destinatario, assunto, corpo)
    else:
        print("❌ Falha ao gerar a resposta com a OpenAI.")
