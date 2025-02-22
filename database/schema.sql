CREATE TABLE IF NOT EXISTS historico_sono (
    id SERIAL PRIMARY KEY,
    usuario_id INT,
    horario_dormir TIME,
    horario_acordar TIME,
    qualidade_sono INT,
    justificativa TEXT,
    avaliacao TEXT,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
