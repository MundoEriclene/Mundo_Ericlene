from backend.send_email_saude import enviar_relatorio_automatico

def avaliar_sono(tempo_sono, qualidade_sono):
    if tempo_sono < 6:
        feedback = "Seu tempo de sono está abaixo do recomendado. Tente dormir pelo menos 7 a 8 horas."
    elif qualidade_sono < 5:
        feedback = "A qualidade do seu sono parece baixa. Evite telas antes de dormir e crie um ambiente confortável."
    else:
        feedback = "Ótimo trabalho! Seu sono está em boas condições."

    # Enviar relatório automático
    enviar_relatorio_automatico("ericlenedesousa@gmail.com", feedback)
    return feedback
