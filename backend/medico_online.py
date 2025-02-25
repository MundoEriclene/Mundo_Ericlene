import openai
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente (caso você esteja usando .env no Render, isso já deve estar configurado)
load_dotenv()

# Configurar a chave da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Função para analisar os dados de sono usando a OpenAI
def analisar_sono_com_openai(dados_sono):
    horario_real = dados_sono.get("horarioReal", "Não informado")
    qualidade_sono = dados_sono.get("qualidadeSono", 0)
    justificativa = dados_sono.get("justificativaSono", "Sem justificativa.")

    # 🔥 Prompts personalizados com base nos dados de sono
    prompt = (
        f"Eu sou um médico especialista em saúde do sono.\n"
        f"Um usuário forneceu os seguintes dados:\n"
        f"- Hora real de sono: {horario_real}\n"
        f"- Qualidade do sono (0-100): {qualidade_sono}\n"
        f"- Justificativa dada pelo usuário: {justificativa}\n\n"
        f"Com base nessas informações, faça uma análise detalhada do sono. "
        f"Dê sugestões personalizadas para melhorar a qualidade do sono e "
        f"explique como a qualidade do sono atual pode afetar a saúde geral.\n"
        f"Forneça a resposta em formato de relatório."
    )

    try:
        # ✅ Enviando o prompt para a OpenAI
        resposta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )

        analise = resposta.choices[0].text.strip()
        return analise

    except Exception as e:
        print(f"🚫 Erro ao analisar dados com a OpenAI: {e}")
        return "Erro ao gerar análise do sono. Tente novamente mais tarde."


# ✅ Função para calcular uma pontuação geral de saúde com base na qualidade do sono
def calcular_saude_percentual(qualidade_sono):
    if qualidade_sono >= 90:
        return 95
    elif qualidade_sono >= 75:
        return 85
    elif qualidade_sono >= 50:
        return 70
    elif qualidade_sono >= 30:
        return 50
    else:
        return 30


# ✅ Função para estimar o impacto do sono na expectativa de vida (simplificado)
def estimar_tempo_vida(qualidade_sono):
    perda_anual_em_anos = (100 - qualidade_sono) * 0.05  # Exemplo simplificado
    expectativa_base = 80  # Expectativa média de vida
    expectativa_final = expectativa_base - perda_anual_em_anos
    return round(expectativa_final, 2)
