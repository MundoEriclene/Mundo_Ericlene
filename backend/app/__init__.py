from flask import Flask

# Criar o app Flask
app = Flask(__name__)

# Registrar blueprints dentro de uma função
def registrar_blueprints():
    from backend.rotasaude import saude_bp  # Importar aqui para evitar importação circular
    app.register_blueprint(saude_bp, url_prefix='/saude')

registrar_blueprints()

# Rota principal
@app.route('/')
def home():
    return "🚀 API Mundo Ericlene funcionando!"

