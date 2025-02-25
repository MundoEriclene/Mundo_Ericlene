import logging
from logging.handlers import RotatingFileHandler
import os

# 📂 Diretório de logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 🔧 Configuração do Logger
def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Criar um handler de console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Definir o formato do log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Adicionar o handler ao logger
    if not logger.hasHandlers():
        logger.addHandler(console_handler)

    return logger

# ✅ Logger principal do aplicativo
app_logger = setup_logger("app")

# ✅ Logger para o envio de e-mails
email_logger = setup_logger("email")

# ✅ Logger para dados de saúde
saude_logger = setup_logger("saude")

# ✅ Logger para relatórios
relatorio_logger = setup_logger("relatorio")

# ✅ Logger para erros gerais
erro_logger = setup_logger("erro")
