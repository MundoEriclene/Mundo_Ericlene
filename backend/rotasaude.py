from flask import Blueprint, request, jsonify
from app import salvar_dados, carregar_dados
from utils import conectar_banco, enviar_email
import openai
import os
# Criar um Blueprint para rotas
rotas = Blueprint('rotas', __name__)

# Rota para salvar dados de sono
@rotas.route('/salvar/sono', methods=['POST'])
def salvar_sono():
    dados = request.json
    if not dados:
        return jsonify({'erro': 'Nenhum dado recebido'}), 400
    salvar_dados('sono', dados)
    return jsonify({'mensagem': 'Dados de sono salvos com sucesso!'}), 200

# Rota para carregar dados de sono
@rotas.route('/carregar/sono', methods=['GET'])
def carregar_sono():
    dados = carregar_dados('sono')
    return jsonify(dados if dados else {}), 200

# Rota para salvar dados de alimentação
@rotas.route('/salvar/alimentacao', methods=['POST'])
def salvar_alimentacao():
    dados = request.json
    if not dados:
        return jsonify({'erro': 'Nenhum dado recebido'}), 400
    salvar_dados('alimentacao', dados)
    return jsonify({'mensagem': 'Dados de alimentação salvos com sucesso!'}), 200

# Rota para carregar dados de alimentação
@rotas.route('/carregar/alimentacao', methods=['GET'])
def carregar_alimentacao():
    dados = carregar_dados('alimentacao')
    return jsonify(dados if dados else {}), 200


saude_bp = Blueprint("saude", __name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@saude_bp.route("/sono", methods=["POST"])
def analisar_sono():
    dados = request.json
    horarioDormir = dados.get("horarioDormir")
    horarioAcordar = dados.get("horarioAcordar")
    qualidadeSono = dados.get("qualidadeSono")
    justificativa = dados.get("justificativaSono")

    # Análise com a OpenAI
    prompt = f"Analise os dados de sono:\nDormiu às: {horarioDormir}\nAcordou às: {horarioAcordar}\nQualidade: {qualidadeSono}\nJustificativa: {justificativa}\nDê uma avaliação médica clara."
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    avaliacao = resposta.choices[0].text.strip()

    # Salvar no banco
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sono (horario_dormir, horario_acordar, qualidade, justificativa) VALUES (%s, %s, %s, %s)",
                   (horarioDormir, horarioAcordar, qualidadeSono, justificativa))
    conn.commit()
    cursor.close()
    conn.close()

    # Enviar análise por e-mail
    enviar_email(
        ["teu-email1@gmail.com", "teu-email2@gmail.com"],
        "Análise de Sono",
        avaliacao
    )

    return jsonify({"status": "sucesso", "avaliacao": avaliacao})
