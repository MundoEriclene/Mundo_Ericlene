CREATE TABLE IF NOT EXISTS historico_sono (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL,  -- Definido como NOT NULL por segurança
    horario_dormir TIME NOT NULL,
    horario_acordar TIME NOT NULL,
    qualidade_sono INT CHECK (qualidade_sono BETWEEN 0 AND 100),
    justificativa TEXT,
    avaliacao TEXT DEFAULT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
