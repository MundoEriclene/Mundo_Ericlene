from flask import Flask, jsonify, request
from rotasaude import saude_routes

# Inicializar o aplicativo Flask
app = Flask(__name__)

# Registrar as rotas de saúde
app.register_blueprint(saude_routes, url_prefix='/saude')

# Rota principal de teste
@app.route('/')
def index():
    return jsonify({"mensagem": "API do Mundo Ericlene em funcionamento!"})

# Rodar o aplicativo
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
