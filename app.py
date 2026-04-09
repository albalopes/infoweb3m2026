from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ola')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email')
@app.route('/faleconosco')
@app.route('/contato')
def contato():
    dados = {"nome": "Italo", "email": "italo@email.com"}
    return render_template('contato.html', dados=dados)

@app.route('/usuario', defaults={"nome": "Desconhecido", "sobrenome": "Desconhecido"})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario(nome, sobrenome):
    info = {"nome": nome, "sobrenome": sobrenome}
    return render_template('usuario.html', info=info)


@app.route('/semestre/<int:x>')
def semestre(x):
    dados = {}
    dados["atual"] = x
    dados["anterior"] = x-1
    return render_template('semestre.html', dados=dados)


if __name__ == '__main__':
    app.run()