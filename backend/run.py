from flask import Flask, request, jsonify  # ✅ Adicionado 'jsonify'
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Log de requisição para debug
@app.before_request
def log_request():
    print(f"📥 Requisição recebida: {request.method} {request.url}")

@app.route('/saude/sono', methods=['POST'])
def salvar_sono():
    data = request.get_json()
    if not data:
        return jsonify({"message": "❌ Dados não recebidos."}), 400  # ✅ Retorno em caso de erro

    # Aqui você pode adicionar lógica para salvar os dados no banco de dados
    print(f"✅ Dados recebidos: {data}")
    return jsonify({"message": "Dados de sono salvos com sucesso!"}), 200

@app.route("/")
def home():
    return "🌍 Mundo Ericlene está rodando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # ✅ Define a porta
    app.run(host="0.0.0.0", port=port)  # ✅ Escutando em todas as interfaces
