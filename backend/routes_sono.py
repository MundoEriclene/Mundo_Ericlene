from flask import Blueprint, request, jsonify
from services.medico_online import analisar_sono
from services.maquina_relatorios import gerar_relatorio_sono
from utils.email_sender import enviar_relatorio_email
from utils.validators import validar_dados_sono
from database.models import salvar_dados_sono

# Criando o blueprint para as rotas de sono
sono_bp = Blueprint('sono', __name__)

# Rota para salvar dados de sono e disparar o relatório
@sono_bp.route('/saude/sono', methods=['POST'])
def salvar_sono():
    dados = request.get_json()

    # ✅ Validação de dados recebidos
    if not dados or not validar_dados_sono(dados):
        return jsonify({"message": "❌ Dados de sono inválidos ou incompletos."}), 400

    # ✅ Salvar dados no banco de dados
    try:
        salvar_dados_sono(dados)
    except Exception as e:
        print(f"🚫 Erro ao salvar dados: {e}")
        return jsonify({"message": "Erro ao salvar os dados no banco."}), 500

    # ✅ Análise pelo Médico Online (OpenAI)
    try:
        avaliacao_medica = analisar_sono(dados)
    except Exception as e:
        print(f"🧠 Erro na análise médica: {e}")
        avaliacao_medica = "Não foi possível gerar uma análise detalhada."

    # ✅ Gerar relatório detalhado com base científica
    try:
        relatorio = gerar_relatorio_sono(dados, avaliacao_medica)
    except Exception as e:
        print(f"📊 Erro ao gerar relatório: {e}")
        relatorio = "Erro ao gerar o relatório de saúde."

    # ✅ Enviar o relatório por e-mail
    try:
        enviar_relatorio_email(relatorio)
    except Exception as e:
        print(f"📧 Erro ao enviar o relatório por e-mail: {e}")
        return jsonify({"message": "Erro ao enviar o relatório por e-mail."}), 500

    # ✅ Resposta de sucesso
    return jsonify({
        "message": "✅ Dados de sono salvos, analisados e relatório enviado com sucesso!",
        "avaliacao_medica": avaliacao_medica
    }), 200

# Rota para verificar se o serviço está ativo
@sono_bp.route('/saude/status', methods=['GET'])
def status_sono():
    return jsonify({"status": "🟢 Serviço de sono ativo e funcionando."}), 200
