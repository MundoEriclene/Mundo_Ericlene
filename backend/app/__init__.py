from flask import Flask
from rotasaude import saude_bp

app = Flask(__name__)
app.register_blueprint(saude_bp, url_prefix="/api")
