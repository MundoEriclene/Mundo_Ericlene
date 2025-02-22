from flask import Blueprint, request, jsonify
from backend.config import get_db_connection
from backend.app.maquina_relatorios import gerar_relatorio_sono
from backend.app.medico_online import avaliar_sono_openai

rotasaude = Blueprint('rotasaude', __name__)
saude_bp = Blueprint('saude', __name__)

@rotasaude.route('/sono', methods=['POST'])
def registrar_sono():
    dados = request.json
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO historico_sono (usuario_id, horario_dormir, horario_acordar, qualidade_sono, justificativa)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        1,
        dados['horarioDormir'],
        dados['horarioAcordar'],
        dados['qualidadeSono'],
        dados['justificativaSono']
    ))

    conn.commit()
    cur.close()
    conn.close()

    # Disparar as funções automáticas
    gerar_relatorio_sono(dados)
    avaliar_sono_openai(dados)

    return jsonify({"mensagem": "Dados salvos e análises enviadas por e-mail!"})
@saude_bp.route('/saude/sono', methods=['POST'])
def registrar_sono():
    dados = request.get_json()

    if not dados:
        return jsonify({"message": "Dados inválidos"}), 400

    salvar_dados_sono(dados)

    # Disparar o relatório
    enviar_relatorio_sono(dados)
    enviar_analise_openai(dados)

    return jsonify({"message": "Dados de sono registrados com sucesso!"}), 201