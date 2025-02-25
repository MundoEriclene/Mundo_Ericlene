from flask import Flask
from flask_cors import CORS
from config import Config
from logger import setup_logger
from routes_sono import sono_bp
from routes_email import email_bp
from database import init_db

# Inicializar o app Flask
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Configurar logs
logger = setup_logger()

# Inicializar banco de dados
init_db()

# Registrar Blueprints (rotas separadas)
app.register_blueprint(sono_bp, url_prefix='/saude/sono')
app.register_blueprint(email_bp, url_prefix='/saude/email')

# Middleware para log de requisições
@app.before_request
def log_request():
    logger.info(f"📥 Requisição recebida: {request.method} {request.url}")

# Rota principal para verificar se o servidor está rodando
@app.route('/')
def home():
    logger.info("🏠 Acesso à rota principal.")
    return "🌍 Mundo Ericlene está rodando!"

# Tratamento de erros globais
@app.errorhandler(404)
def not_found_error(error):
    logger.error(f"❌ Rota não encontrada: {request.url}")
    return {"error": "Rota não encontrada."}, 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"💥 Erro interno: {str(error)}")
    return {"error": "Erro interno do servidor."}, 500

# Iniciar a aplicação
if __name__ == '__main__':
    port = int(Config.PORT)
    logger.info(f"🚀 Servidor iniciado na porta {port}")
    app.run(host='0.0.0.0', port=port)
