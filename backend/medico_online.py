import openai
from send_email_saude import enviar_email_relatorio  # Corrigir o nome da função
import os

# Configurar API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("❌ A chave da API da OpenAI não está configurada. Verifique suas variáveis de ambiente.")

def avaliar_sono_openai(dados_sono):
    prompt = f"""
    💤 Avaliação de Sono Personalizada 💤

    Dados fornecidos:
    - Horário de dormir: {dados_sono.get('horarioDormir')}
    - Horário de acordar: {dados_sono.get('horarioAcordar')}
    - Qualidade do sono (0-100): {dados_sono.get('qualidadeSono')}
    - Justificativa: {dados_sono.get('justificativaSono')}

    Baseando-se nesses dados, forneça um parecer médico personalizado sobre a qualidade do sono, possíveis causas para a pontuação indicada e recomendações para melhorias na rotina de sono.
    """

    try:
        resposta = openai.Completion.create(
            model="text-davinci-003",  # Altere para "gpt-3.5-turbo" se necessário
            prompt=prompt,
            max_tokens=200
        )

        avaliacao = resposta.choices[0].text.strip()

        # Enviar a avaliação por e-mail
        enviar_email_relatorio(
            assunto="🩺 Avaliação Médica Personalizada do Sono",
            mensagem=avaliacao
        )
        print("✅ Avaliação enviada por e-mail com sucesso.")

    except openai.error.OpenAIError as e:
        print(f"❌ Erro na API da OpenAI: {e}")

    except Exception as e:
        print(f"❌ Erro inesperado ao avaliar o sono: {e}")
