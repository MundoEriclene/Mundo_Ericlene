from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from send_email_saude import enviar_relatorio  # ✅ Importação para envio de e-mail

app = Flask(__name__)
CORS(app)

# Log de requisição para debug
@app.before_request
def log_request():
    print(f"📥 Requisição recebida: {request.method} {request.url}")

# Rota para salvar dados de sono e enviar e-mail
@app.route('/saude/sono', methods=['POST'])
def salvar_sono():
    data = request.get_json()
    if not data:
        return jsonify({"message": "❌ Dados não recebidos."}), 400

    try:
        # 🚩 Lógica para salvar os dados no banco de dados (simulada por enquanto)
        print(f"✅ Dados recebidos: {data}")

        # 🚀 Envio de relatório por e-mail
        enviar_relatorio(data)  # Chama a função de envio

        return jsonify({"message": "✅ Dados de sono salvos e e-mail enviado com sucesso!"}), 200
    except Exception as e:
        print(f"🚫 Erro ao processar dados: {str(e)}")
        return jsonify({"message": f"Erro ao salvar os dados ou enviar e-mail: {str(e)}"}), 500

# Rota principal para verificar se o servidor está rodando
@app.route("/")
def home():
    return "🌍 Mundo Ericlene está rodando!"

# Configuração da porta e execução do servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # ✅ Define a porta
    app.run(host="0.0.0.0", port=port)  # ✅ Escutando em todas as interfaces
