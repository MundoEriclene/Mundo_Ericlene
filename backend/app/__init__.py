from flask import Flask

# Criar o app Flask
app = Flask(__name__)

# Registrar blueprints
def registrar_blueprints():
    from backend.rotasaude import saude_bp  # Importação corrigida
    app.register_blueprint(saude_bp, url_prefix='/saude')

registrar_blueprints()

# Rota principal
@app.route('/')
def home():
    return "🚀 API Mundo Ericlene funcionando!"
