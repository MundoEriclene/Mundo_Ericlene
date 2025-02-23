from flask import Blueprint, request, jsonify
from app.config import get_db_connection
from app.maquina_relatorios import gerar_relatorio_sono
from app.medico_online import avaliar_sono_openai

# Definindo as Blueprints
saude_bp = Blueprint('saude', __name__)

# Rota para registrar dados de sono
@saude_bp.route('/sono', methods=['POST'])
def registrar_sono():
    dados = request.get_json()

    if not dados:
        return jsonify({"message": "Dados inválidos"}), 400

    # Verificando a presença de todos os campos
    campos_necessarios = ['horarioReal', 'qualidadeSono', 'justificativaSono']
    if not all(campo in dados for campo in campos_necessarios):
        return jsonify({"message": "Campos obrigatórios ausentes."}), 400

    # Conexão com o banco de dados
    try:
        conn = get_db_connection()
        if conn is None:
            raise ValueError("Conexão com o banco falhou.")

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO historico_sono (usuario_id, horario_real, qualidade_sono, justificativa)
            VALUES (%s, %s, %s, %s)
        """, (
            1,  # ID do usuário fixo por enquanto
            dados['horarioReal'],
            dados['qualidadeSono'],
            dados['justificativaSono']
        ))

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao salvar no banco de dados: {e}")
        return jsonify({"message": "Erro ao salvar os dados."}), 500

    # Funções de relatório e análise com OpenAI
    try:
        gerar_relatorio_sono(dados)
        avaliar_sono_openai(dados)
    except Exception as e:
        print(f"Erro ao enviar relatório ou análise: {e}")
        return jsonify({"message": "Dados salvos, mas houve erro no envio do relatório."}), 500

    return jsonify({"message": "Dados de sono registrados com sucesso e análises enviadas por e-mail!"}), 201
