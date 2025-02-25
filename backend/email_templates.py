from datetime import datetime

# 📆 Função para gerar o assunto do e-mail
def gerar_assunto_relatorio():
    data_atual = datetime.now().strftime("%d/%m/%Y")
    return f"📊 Relatório de Saúde - {data_atual}"

# 📝 Função para gerar o corpo do relatório
def gerar_mensagem_relatorio(nome, dados_sono, avaliacao_medica):
    horario_real = dados_sono.get('horarioReal', 'Não informado')
    qualidade = dados_sono.get('qualidadeSono', 'Não informado')
    justificativa = dados_sono.get('justificativaSono', 'Não informada')

    return f"""
    Olá, {nome}!

    Aqui está o seu relatório de saúde com base nos dados que você forneceu:

    🛌 **Dados de Sono**:
    - Hora real de sono: {horario_real}
    - Qualidade do sono: {qualidade}%
    - Justificativa da avaliação: {justificativa}

    💡 **Avaliação Médica Personalizada**:
    {avaliacao_medica}

    🔍 **Recomendações**:
    - Tente manter um horário regular para dormir.
    - Busque atingir uma qualidade de sono acima de 75%.
    - Evite o uso de eletrônicos 30 minutos antes de dormir.

    🤖 Este relatório foi gerado automaticamente pela sua Máquina de Saúde do Mundo Ericlene.

    Se precisar de mais informações ou ajuda, não hesite em entrar em contato!

    Abraços,  
    🌍 Mundo Ericlene
    """

# 🔔 Função para mensagem de confirmação de envio de e-mail
def mensagem_sucesso_envio(destinatario):
    return f"E-mail enviado com sucesso para {destinatario} ✅"

# ⚠️ Função para mensagem de falha no envio de e-mail
def mensagem_erro_envio(erro):
    return f"❌ Ocorreu um erro ao enviar o e-mail: {erro}"

# 📉 Função para notificar baixa qualidade de sono
def alerta_baixa_qualidade(qualidade):
    if qualidade < 50:
        return (
            "⚠️ Atenção: Sua qualidade de sono está baixa! "
            "Considere melhorar seus hábitos de sono para evitar impactos na sua saúde."
        )
    return ""
