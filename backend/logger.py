import logging
from logging.handlers import RotatingFileHandler
import os

# 📂 Diretório de logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 🔧 Configuração do Logger
def configurar_logger(nome_logger):
    logger = logging.getLogger(nome_logger)
    logger.setLevel(logging.DEBUG)  # 🔍 Níveis de log: DEBUG, INFO, WARNING, ERROR, CRITICAL

    # 🗂️ Configuração do arquivo de log rotativo
    log_file = os.path.join(LOG_DIR, f"{nome_logger}.log")
    file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    # 🖨️ Configuração do formato do log
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )
    file_handler.setFormatter(formatter)

    # 📤 Configuração para exibir logs no console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 🔗 Adicionando handlers ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# ✅ Logger principal do aplicativo
app_logger = configurar_logger("app")

# ✅ Logger para o envio de e-mails
email_logger = configurar_logger("email")

# ✅ Logger para dados de saúde
saude_logger = configurar_logger("saude")

# ✅ Logger para relatórios
relatorio_logger = configurar_logger("relatorio")

# ✅ Logger para erros gerais
erro_logger = configurar_logger("erro")
