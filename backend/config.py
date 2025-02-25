import os

class Config:
    # Configuração básica do Flask
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'minha_chave_secreta')

    # Configuração de CORS
    CORS_HEADERS = 'Content-Type'

    # Configuração do Banco de Dados PostgreSQL no Render
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://usuario:senha@localhost:5432/mundo_ericlene')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração de E-mail (Gmail SMTP)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER', 'mundoericlene@gmail.com')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS', 'senha_do_gmail')

    # Configurações personalizadas do projeto
    DEFAULT_RECIPIENTS = os.environ.get('RECIPIENTS', 'ericlenedesousa@gmail.com,norquenialopes90@gmail.com').split(',')
    MAX_SONO_QUALIDADE = 100  # Limite máximo de qualidade de sono

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

# Dicionário de configuração
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
