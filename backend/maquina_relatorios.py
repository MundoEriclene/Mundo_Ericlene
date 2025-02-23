from datetime import datetime, timedelta
from app.send_emal_saude import enviar_email_relatorio  # Corrigida a importação

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
    try:
        # Converte as strings de horário para datetime
        horario_dormir = datetime.strptime(dados_sono.get("horarioDormir"), "%H:%M")
        horario_acordar = datetime.strptime(dados_sono.get("horarioAcordar"), "%H:%M")

        # Ajusta caso tenha dormido após a meia-noite
        if horario_acordar <= horario_dormir:
            horario_acordar += timedelta(days=1)

        # Calcula a duração do sono
        tempo_sono = (horario_acordar - horario_dormir).seconds / 3600  # Em horas

        # Cálculo de saúde e tempo de vida
        saude, anos_adicionados = calcular_saude_e_tempo(tempo_sono)
        expectativa_vida_base = 79  # Valor padrão de expectativa de vida
        estimativa_vida = expectativa_vida_base + anos_adicionados

        # Gera o relatório
        relatorio = f"""
        💤 Relatório Diário de Sono 💤

        ⏰ Horário de dormir: {dados_sono.get('horarioDormir')}
        ⏰ Horário de acordar: {dados_sono.get('horarioAcordar')}
        😴 Duração do sono: {tempo_sono:.2f} horas
        ✅ Saúde atual: {saude}%
        🕒 Expectativa de vida estimada: {estimativa_vida:.2f} anos
        """

        # Enviar e-mail com o relatório
        enviar_email_relatorio(
            assunto="📊 Relatório Diário de Sono",
            mensagem=relatorio
        )

        return relatorio  # Retorna o relatório em caso de sucesso

    except ValueError as e:
        print(f"❌ Erro ao converter horários: {e}")
        return None

    except Exception as e:
        print(f"❌ Erro inesperado ao gerar relatório: {e}")
        return None
