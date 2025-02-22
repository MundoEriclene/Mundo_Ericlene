from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Log de requisição para debug
@app.before_request
def log_request():
    print(f"Requisição recebida: {request.method} {request.url}")
