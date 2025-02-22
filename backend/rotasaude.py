from flask import Blueprint, request, jsonify

# Criar um Blueprint para as rotas de saúde
saude_bp = Blueprint('saude', __name__)

# Rota para salvar dados de saúde
@saude_bp.route('/salvar', methods=['POST'])
def salvar_dados():
    dados = request.json
    # Aqui, você pode adicionar a lógica de salvar os dados no banco
    return jsonify({'mensagem': '✅ Dados de saúde salvos com sucesso!'})

# Rota para carregar dados de saúde
@saude_bp.route('/carregar', methods=['GET'])
def carregar_dados():
    # Exemplo de dados de saúde
    dados = {
        "sono": 8,
        "exercicio": "corrida",
        "alimentacao": "balanceada"
    }
    return jsonify(dados)
