from flask import Blueprint, request, jsonify
from app import salvar_dados, carregar_dados

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
