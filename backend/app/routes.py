from flask import Blueprint, request, jsonify
from backend.avaliador_sono import avaliar_sono

rotas_sono = Blueprint('rotas_sono', __name__)

@rotas_sono.route('/avaliar_sono', methods=['POST'])
def avaliar_sono_route():
    data = request.get_json()
    tempo_sono = data.get('tempo_sono')
    qualidade_sono = data.get('qualidade_sono')

    if tempo_sono is None or qualidade_sono is None:
        return jsonify({"erro": "Os dados de sono são obrigatórios."}), 400

    resultado = avaliar_sono(tempo_sono, qualidade_sono)
    return jsonify({"mensagem": resultado}), 200
