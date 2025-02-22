from flask import Blueprint, request, jsonify
from app.config import get_db_connection
import openai
import os

# Configurar API Key da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

rotasaude = Blueprint('rotasaude', __name__)

# Função para enviar dados à OpenAI
def avaliar_sono(texto):
    resposta = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Avalie a qualidade do sono com base nessas informações: {texto}",
        max_tokens=150
    )
    return resposta.choices[0].text.strip()

# Rota para receber dados de sono
@rotasaude.route('/sono', methods=['POST'])
def registrar_sono():
    dados = request.json
    conn = get_db_connection()
    cur = conn.cursor()

    avaliacao = avaliar_sono(
        f"Horário de dormir: {dados['horarioDormir']}, "
        f"Horário de acordar: {dados['horarioAcordar']}, "
        f"Qualidade do sono: {dados['qualidadeSono']}, "
        f"Justificativa: {dados['justificativaSono']}"
    )

    cur.execute("""
        INSERT INTO historico_sono (usuario_id, horario_dormir, horario_acordar, qualidade_sono, justificativa, avaliacao)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (1, dados['horarioDormir'], dados['horarioAcordar'], dados['qualidadeSono'], dados['justificativaSono'], avaliacao))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Dados de sono salvos com sucesso!", "avaliacao": avaliacao})
