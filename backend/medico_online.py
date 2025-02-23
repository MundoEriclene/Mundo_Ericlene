import openai
from app.send_emal_saude import enviar_email_relatorio  # Corrigido o nome da função
import os

# Configurar API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("❌ A chave da API da OpenAI não está configurada. Verifique suas variáveis de ambiente.")

def avaliar_sono_openai(dados_sono):
    # Garantir que todos os dados necessários estão presentes
    horario_dormir = dados_sono.get('horarioDormir', 'Não informado')
    horario_acordar = dados_sono.get('horarioAcordar', 'Não informado')
    qualidade_sono = dados_sono.get('qualidadeSono', 'Não informado')
    justificativa = dados_sono.get('justificativaSono', 'Não informado')

    prompt = f"""
    💤 Avaliação de Sono Personalizada 💤

    Dados fornecidos:
    - Horário de dormir: {horario_dormir}
    - Horário de acordar: {horario_acordar}
    - Qualidade do sono (0-100): {qualidade_sono}
    - Justificativa: {justificativa}

    Baseando-se nesses dados, forneça um parecer médico personalizado sobre a qualidade do sono, possíveis causas para a pontuação indicada e recomendações baseadas em estudos científicos sobre os efeitos do sono de menos de 8 horas ou mais de 9 horas.
    """

    try:
        resposta = openai.Completion.create(
            model="text-davinci-003",  # Pode ser atualizado para "gpt-3.5-turbo" com ajustes na API
            prompt=prompt,
            max_tokens=500
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
