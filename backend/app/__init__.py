from flask import Flask
from backend.app.routes import rotas_sono

def criar_app():
    app = Flask(__name__)
    app.register_blueprint(rotas_sono)
    return app

# Criar o app Flask
app = Flask(__name__)

# Registrar blueprints
def registrar_blueprints():
    from rotasaude import saude_bp  # Importação corrigida
    app.register_blueprint(saude_bp, url_prefix='/saude')

registrar_blueprints()

# Rota principal
@app.route('/')
def home():
    return "🚀 API Mundo Ericlene funcionando!"
