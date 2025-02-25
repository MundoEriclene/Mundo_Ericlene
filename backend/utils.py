import datetime
from dateutil import parser
from pydantic import BaseModel, ValidationError, validator
from email_validator import validate_email, EmailNotValidError


# ✅ Classe de validação de dados usando Pydantic
class SonoData(BaseModel):
    horario_real: str
    qualidade_sono: int
    justificativa: str

    @validator("horario_real")
    def validar_horario_real(cls, value):
        try:
            parser.parse(value)
            return value
        except ValueError:
            raise ValueError("❌ Horário real de sono inválido.")

    @validator("qualidade_sono")
    def validar_qualidade(cls, value):
        if 0 <= value <= 100:
            return value
        raise ValueError("❌ A qualidade do sono deve estar entre 0 e 100.")

    @validator("justificativa")
    def validar_justificativa(cls, value):
        if not value.strip():
            raise ValueError("❌ A justificativa não pode estar vazia.")
        return value


# 🕒 Função para calcular a duração do sono
def calcular_duracao_sono(horario_inicio: str, horario_fim: str) -> float:
    try:
        inicio = parser.parse(horario_inicio)
        fim = parser.parse(horario_fim)
        duracao = (fim - inicio).total_seconds() / 3600  # Converter para horas
        return max(0, duracao)  # Garante que a duração não seja negativa
    except ValueError:
        return 0.0


# 📊 Função para calcular a pontuação de saúde com base no sono
def calcular_saude_percentual(qualidade_sono: int, horas_dormidas: float) -> float:
    ideal_horas = 8
    penalidade = abs(ideal_horas - horas_dormidas) * 5  # Penalidade de 5% por hora fora do ideal
    saude = max(0, min(100, qualidade_sono - penalidade))
    return round(saude, 2)


# ⏳ Função para estimar a expectativa de vida com base no sono
def estimar_expectativa_vida(saude_percentual: float) -> float:
    vida_maxima = 85  # Expectativa média de vida em anos
    reducao = (100 - saude_percentual) * 0.2  # Reduz 0.2 anos por ponto percentual abaixo de 100%
    expectativa = max(0, vida_maxima - reducao)
    return round(expectativa, 1)


# ✉️ Função para validar e-mails
def validar_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


# 📝 Função para formatar relatório de sono
def formatar_relatorio_sono(horas_dormidas, qualidade, saude_percentual, expectativa_vida):
    return f"""
    💤 Relatório de Sono - Mundo Ericlene 💤

    ✅ Horas dormidas: {horas_dormidas:.2f} horas
    ✅ Qualidade do sono: {qualidade}%
    ✅ Saúde geral com base no sono: {saude_percentual}%
    ✅ Expectativa de vida estimada: {expectativa_vida} anos

    🔍 Recomendações:
    - Tente manter uma rotina de sono consistente.
    - Evite cafeína antes de dormir.
    - Pratique exercícios regularmente para melhorar a qualidade do sono.

    🌟 Cuide-se e mantenha hábitos saudáveis!
    """


# 📅 Função para obter o horário atual formatado
def horario_atual_formatado() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
