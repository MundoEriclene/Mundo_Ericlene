from flask import Flask
from rotasaude import saude_bp  # Importa o blueprint de rotasaude

# Criar o app Flask
app = Flask(__name__)

# Registrar o blueprint de saúde
app.register_blueprint(saude_bp, url_prefix='/saude')

# Rota principal
@app.route('/')
def home():
    return "🚀 API Mundo Ericlene funcionando!"

# Inicializar o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
