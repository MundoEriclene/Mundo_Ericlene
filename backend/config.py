import os
import psycopg2
from psycopg2.extras import RealDictCursor

# URL do banco de dados do Render
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://mundo_ericlene_user:oTN0z87KpWPHpEcXeW5pHpe8ne5EdhMX@dpg-cut0bktumphs73cdsm40-a/mundo_ericlene"
)

# Função de conexão
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"Erro de conexão com o banco de dados: {e}")
        return None
