from app import app  # Remover 'backend.' do import

# Rodar o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
