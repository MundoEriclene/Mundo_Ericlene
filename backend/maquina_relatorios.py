from medico_online import analisar_sono_com_openai, calcular_saude_percentual, estimar_tempo_vida
import datetime

# ✅ Função principal para gerar o relatório completo
def gerar_relatorio_sono(dados_sono):
    horario_real = dados_sono.get("horarioReal", "Não informado")
    qualidade_sono = dados_sono.get("qualidadeSono", 0)
    justificativa = dados_sono.get("justificativaSono", "Sem justificativa.")

    # 🔍 Análise detalhada usando a OpenAI
    analise_detalhada = analisar_sono_com_openai(dados_sono)

    # 📊 Cálculos de saúde e expectativa de vida
    saude_percentual = calcular_saude_percentual(qualidade_sono)
    expectativa_vida = estimar_tempo_vida(qualidade_sono)

    # 📅 Data do relatório
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    # 📝 Estrutura do relatório
    relatorio = f"""
    📅 **Relatório de Sono - {data_atual}**

    🕒 **Informações Registradas:**
    - Hora real de sono: {horario_real}
    - Qualidade do sono: {qualidade_sono}%
    - Justificativa: {justificativa}

    🩺 **Análise Médica:**
    {analise_detalhada}

    💡 **Resumo de Saúde:**
    - Saúde geral estimada: {saude_percentual}%
    - Expectativa de vida projetada: {expectativa_vida} anos

    🔔 **Recomendações:**
    - Tente manter uma rotina de sono consistente.
    - Evite o uso de eletrônicos antes de dormir.
    - Hidrate-se bem durante o dia e pratique exercícios físicos regularmente.
    """

    return relatorio


# ✅ Função para criar um assunto de e-mail personalizado
def gerar_assunto_relatorio():
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    return f"📧 Relatório de Saúde do Sono - {data_atual}"


# ✅ Função para logar o relatório no console (para debug)
def logar_relatorio(relatorio):
    print("📝 Relatório Gerado:")
    print("=" * 40)
    print(relatorio)
    print("=" * 40)
