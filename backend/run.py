from flask import Flask
from backend.rotasaude import rotasaude
from app import app

app = Flask(__name__)
app.register_blueprint(rotasaude)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
