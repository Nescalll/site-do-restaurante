from flask import Flask, render_template, request, redirect, url_for, flash
from models import Usuario, Produto, ItemPedido, Pedido
from db import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'lancode'
lm = LoginManager(app)
lm.login_view = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)

def usuario_logado():
    return current_user.is_authenticated

@lm.user_loader
def user_loadere(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario

@app.route("/", methods=['GET', 'POST'])
def principal():
    mensagem = 'deslogar'
    if (not usuario_logado()):
        mensagem = 'login'

    if(request.method == "GET"):
        return render_template('index.html', mensagem=mensagem)
    
    elif(request.method == "POST"):
        if('botaoDeslogarLogar' in request.form):
            if (usuario_logado()): 
                logout_user()
                return render_template('index.html', mensagem='login')
            return redirect(url_for('login'))
        elif('botaoParaCarrinho' in request.form):
            return redirect(url_for('carrinho'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']
        user = db.session.query(Usuario).filter_by(nome=nome, senha=senha).first()
        if not user:
            return render_template('login.html', mensagem="Usuario ou senha não encontrados")
        login_user(user)
        return redirect(url_for('principal', mensagem='deslogar'))
    elif request.method == 'GET':
        return render_template('login.html')
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template("registrar.html")
    
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmacao_senha = request.form['confirmar_senha']
        confirmacao_email = db.session.query(Usuario).filter_by(email=email).first()
        if (senha != confirmacao_senha):
            return render_template('registrar.html', mensagem="senha diferentes foram digitadas")
        if (confirmacao_email):
            return render_template('registrar.html', mensagem="este E-mail já está cadastrado")
        novo_usuario = Usuario(nome=nome, senha=senha, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        login_user(novo_usuario)
        return redirect(url_for('principal', mensagem='deslogar'))
@app.route('/carrinho', methods=['GET', 'POST'])
@login_required
def carrinho():
    usuario_id = current_user.id
    if(request.method == "POST"):
        botaoAtivado = request.form.get('botao').split('-')
        produto_atualizar = db.session.query(ItemPedido).filter_by(id=int(botaoAtivado[1])).first() 
        if ("add" in botaoAtivado):
            produto_atualizar.quantidade += 1
            db.session.commit()
        elif ("ret" in botaoAtivado):
            produto_atualizar.quantidade -= 1
            if(produto_atualizar.quantidade == 0):
                db.session.delete(produto_atualizar)
            db.session.commit()
        elif ("del" in botaoAtivado):
            db.session.delete(produto_atualizar)
            db.session.commit()

    historico_visivel=[]
    historico = db.session.query(ItemPedido).filter_by(pedido_id=usuario_id).all()
    for produto in historico:
        produto_visivel = db.session.query(Produto).filter_by(id=produto.id).first()
        historico_visivel.append({'nome':produto_visivel.nome, "valor":produto_visivel.valor, "quantidade":produto.quantidade, "ilustracao":produto_visivel.ilustracao, "id":produto.id})
    return render_template('carrinho.html', carrinho=historico_visivel)
@app.route('/cardapio', methods=['GET', 'POST'])
def cardapio():
    usuario_id = current_user.id
    all_produtos = []
    produtos = db.session.query(Produto)
    for produto in produtos:
        all_produtos.append({'nome':produto.nome, 'valor':produto.valor, 'id':produto.id, 'ilustracao':produto.ilustracao})
    if (request.method == "POST"):
        botaoAtivado = request.form.get('botao').split('-')
        print(botaoAtivado)
        idDoProduto = int(botaoAtivado[1])
        produto_pedido = db.session.query(Produto).filter_by(id=idDoProduto).first()
        pedidoDoUsuario = db.session.query(Pedido).filter_by(id=idDoProduto).first()
        pedidoExistente = db.session.query(ItemPedido).filter_by(id=usuario_id).first()
        if (not pedidoDoUsuario):
            novo_pedido = Pedido(usuario_id = usuario_id, total=produto_pedido.valor)
            novo_item = ItemPedido(produto_id=produto_pedido.id, quantidade=1, preco_unitario=produto_pedido.valor)
            db.session.add(novo_pedido)
            db.session.add(novo_item)
        if(not pedidoExistente):
            pedidoDoUsuario.total += produto_pedido.valor
            db.session.commit()
            novo_item = ItemPedido(produto_id=produto_pedido.id, quantidade=1, preco_unitario=produto_pedido.valor)
            db.session.add(novo_item)
            db.session.commit()
        else:
            pedidoDoUsuario.total += produto_pedido.valor
            db.session.commit()
            pedidoExistente.quantidade += 1
            db.session.commit()
        return render_template('cardapio.html', produtos=all_produtos)
    return render_template('cardapio.html', produtos=all_produtos)

if(__name__ == '__main__'):
    with app.app_context():
        db.create_all()
    app.run(debug=True)
