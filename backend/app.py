from flask import Flask
from rotasaude import saude_bp  # Importando blueprint

# Criar o app Flask
app = Flask(__name__)

# Registrar o blueprint de saúde
app.register_blueprint(saude_bp, url_prefix='/saude')

# Rota principal
@app.route('/')
def home():
    return "🚀 API Mundo Ericlene funcionando!"
