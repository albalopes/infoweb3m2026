from flask import Flask, render_template, request
from datetime import datetime

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

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['GET', 'POST'])
def recebedados():
    nome = request.form.get('nome')
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    datanasc = request.form['datanasc']
    data_objeto = datetime.strptime(datanasc, "%Y-%m-%d")
    data_formatada = data_objeto.strftime("%d-%m-%Y")
    estado = request.form.get('estado')
    escola = request.form.getlist('escola')

    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email, datanasc=data_formatada, estado=estado, escola=escola)

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/recebecompras', methods=['POST'])
def recebecompras():
    itens = request.form.getlist('item')
    return render_template('lista.html', itens=itens)

if __name__ == '__main__':
    app.run()