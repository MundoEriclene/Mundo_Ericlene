from flask import Flask, request  # ✅ Adicionado 'request' aqui
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Log de requisição para debug
@app.before_request
def log_request():
    print(f"📥 Requisição recebida: {request.method} {request.url}")

@app.route("/")
def home():
    return "🌍 Mundo Ericlene está rodando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # ✅ Define a porta
    app.run(host="0.0.0.0", port=port)  # ✅ Escutando em todas as interfaces
