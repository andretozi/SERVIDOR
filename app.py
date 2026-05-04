from flask import Flask
# Importando da pasta 'controllers' diretamente
from controllers.livro_controller import livro_bp

app = Flask(__name__)

app.register_blueprint(livro_bp)

if __name__ == '__main__':

    app.run(port=5000, debug=True)