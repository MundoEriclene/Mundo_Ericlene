from flask import Blueprint, request, jsonify
from utils.email_sender import enviar_email_personalizado
from utils.validators import validar_dados_email

# Criando o blueprint para rotas de e-mail
email_bp = Blueprint('email', __name__)

# ✅ Rota para enviar e-mail manualmente
@email_bp.route('/email/enviar', methods=['POST'])
def enviar_email():
    dados = request.get_json()

    # ✅ Validação dos dados do e-mail
    if not dados or not validar_dados_email(dados):
        return jsonify({"message": "❌ Dados de e-mail inválidos ou incompletos."}), 400

    destinatario = dados.get("destinatario")
    assunto = dados.get("assunto")
    corpo = dados.get("corpo")

    # ✅ Tentando enviar o e-mail
    try:
        enviar_email_personalizado(destinatario, assunto, corpo)
    except Exception as e:
        print(f"🚫 Erro ao enviar e-mail: {e}")
        return jsonify({"message": "Erro ao enviar o e-mail."}), 500

    return jsonify({"message": "✅ E-mail enviado com sucesso!"}), 200


# ✅ Rota de teste para verificar se o envio de e-mails funciona
@email_bp.route('/email/teste', methods=['GET'])
def teste_email():
    destinatario = "mundoericlene@gmail.com"
    assunto = "🚀 Teste de Envio de E-mail"
    corpo = "Este é um e-mail de teste do sistema de relatórios do Mundo Ericlene."

    try:
        enviar_email_personalizado(destinatario, assunto, corpo)
    except Exception as e:
        print(f"🚫 Erro ao enviar e-mail de teste: {e}")
        return jsonify({"message": "Erro ao enviar o e-mail de teste."}), 500

    return jsonify({"message": "✅ E-mail de teste enviado com sucesso!"}), 200


# ✅ Rota para reenviar um relatório manualmente
@email_bp.route('/email/reenviar-relatorio', methods=['POST'])
def reenviar_relatorio():
    dados = request.get_json()

    if not dados or not validar_dados_email(dados):
        return jsonify({"message": "❌ Dados de e-mail inválidos ou incompletos."}), 400

    destinatario = dados.get("destinatario")
    relatorio = dados.get("relatorio")

    if not relatorio:
        return jsonify({"message": "❌ Nenhum relatório fornecido para envio."}), 400

    try:
        enviar_email_personalizado(destinatario, "📋 Reenvio de Relatório de Saúde", relatorio)
    except Exception as e:
        print(f"🚫 Erro ao reenviar relatório: {e}")
        return jsonify({"message": "Erro ao reenviar o relatório."}), 500

    return jsonify({"message": "✅ Relatório reenviado com sucesso!"}), 200
