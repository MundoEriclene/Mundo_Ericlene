from datetime import datetime
from send_email_saude import enviar_email

def calcular_saude_e_tempo(tempo_sono):
    if tempo_sono >= 8:
        anos_adicionados = 0.2  # Cada boa noite de sono adiciona 0.2 anos
        saude_percentual = 100
    elif 6 <= tempo_sono < 8:
        anos_adicionados = 0
        saude_percentual = 90
    else:
        anos_adicionados = -0.1  # Reduz 0.1 anos
        saude_percentual = 80

    return saude_percentual, anos_adicionados

def gerar_relatorio_sono(dados_sono):
    tempo_sono = dados_sono.get("horarioAcordar") - dados_sono.get("horarioDormir")
    horas_sono = tempo_sono.total_seconds() / 3600

    saude, anos_adicionados = calcular_saude_e_tempo(horas_sono)
    estimativa_vida = 79 + anos_adicionados

    relatorio = f"""
    💤 Relatório Diário de Sono 💤

    ⏰ Horário de dormir: {dados_sono.get('horarioDormir')}
    ⏰ Horário de acordar: {dados_sono.get('horarioAcordar')}
    😴 Duração do sono: {horas_sono:.2f} horas
    ✅ Saúde atual: {saude}%
    🕒 Expectativa de vida estimada: {estimativa_vida:.2f} anos
    """

    # Enviar e-mail com o relatório
    enviar_email(
        assunto="Relatório Diário de Sono",
        mensagem=relatorio
    )
