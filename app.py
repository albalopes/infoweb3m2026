from flask import Flask

app = Flask(__name__)

@app.route('/ola')
@app.route('/')
def index():
    return 'Programação de Aplicação Web é a melhor disciplina do mundo!'