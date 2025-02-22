import openai
from send_email_saude import enviar_email
import os

# Configurar API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def avaliar_sono_openai(dados_sono):
    prompt = f"""
    Avalie a qualidade do sono com base nos seguintes dados:
    - Horário de dormir: {dados_sono.get('horarioDormir')}
    - Horário de acordar: {dados_sono.get('horarioAcordar')}
    - Qualidade do sono: {dados_sono.get('qualidadeSono')}
    - Justificativa: {dados_sono.get('justificativaSono')}

    Dê um parecer médico sobre a saúde do sono e recomendações.
    """

    resposta = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    avaliacao = resposta.choices[0].text.strip()

    # Enviar a avaliação por e-mail
    enviar_email(
        assunto="Avaliação Médica do Sono",
        mensagem=avaliacao
    )
