from flask import Blueprint, request, jsonify

# Criar o Blueprint
saude_bp = Blueprint('saude', __name__)

# Definir rotas
@saude_bp.route('/salvar', methods=['POST'])
def salvar_dados():
    dados = request.json
    # Aqui, você adicionará a lógica para salvar no banco de dados
    return jsonify({'mensagem': 'Dados salvos com sucesso!'})

@saude_bp.route('/carregar', methods=['GET'])
def carregar_dados():
    # Aqui, você adicionará a lógica para carregar do banco de dados
    dados = {"sono": 8, "exercicio": "corrida"}
    return jsonify(dados)
