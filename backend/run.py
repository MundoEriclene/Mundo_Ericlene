from backend.app import app  # Agora importando com o caminho correto

# Rodar o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
