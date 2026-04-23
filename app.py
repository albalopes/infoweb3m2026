from flask import Flask, render_template, request, redirect, url_for
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


@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'Você é MAIOR de idade'
    else:
        return 'Você é MENOR de idade'

@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form.get('login')
    senha = request.form.get('senha')
    if usuario=='admin' and senha=='12345':
        return redirect(url_for('arearestrita'))
    else:
        return redirect(url_for('acessonegado'))

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')

@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')

@app.route('/produtos')
def produtos():
    
    itens = [
        {"nome": "Teclado", "preco": "200", "categoria": "computador", "imagem":"https://m.media-amazon.com/images/I/61B8ljXNedL._AC_SX569_.jpg"},
        {"nome": "Smartphone", "preco": "1500", "categoria":"celular", "imagem":"https://m.media-amazon.com/images/I/51k0qRQFcuL._AC_SL1000_.jpg"},
        {"nome": "Pen-drive 1", "preco": "50", "categoria": "computador", "imagem":"https://m.media-amazon.com/images/I/51e8li2lxDL._AC_SY300_SX300_QL70_ML2_.jpg"}
    ]

    qtd = len(itens)

    return render_template('produtos.html', itens=itens, qtd=qtd)


if __name__ == '__main__':
    app.run()