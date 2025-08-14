from main import app, db
from models import Produto, Usuario, ItemPedido, Pedido

with app.app_context():
    subcategoria = "sobremesas"
    '''produtos =[{'nome': 'Vinho Le Mortelle' , 'valor':350.50, 'subcategoria':subcategoria, 'ilustracao':'vinho.jpg' },
               {'nome':'Champgne Bollinger' , 'valor':750.00, 'subcategoria':subcategoria, 'ilustracao':'champgne.jpg'},
               {'nome':'Cerveja Skol de garrafa' , 'valor':11.00, 'subcategoria':subcategoria, 'ilustracao':'cerveja skol.jpg'},
               {'nome':'Cerveja Amistel de latinha' , 'valor':8.00, 'subcategoria':subcategoria, 'ilustracao' :'cerveja amistel.jpg'},
               {'nome':'Coca-Cola 1L' , 'valor': 10.00, 'subcategoria':subcategoria, 'ilustracao':'Coca-cola de garrafa.jpg'},
               {'nome':'Coca-Cola latinha' , 'valor':6.00, 'subcategoria':subcategoria, 'ilustracao':'Coca-Cola.jpg'},
               {'nome':'Pepsi 1L' , 'valor':9.50, 'subcategoria':subcategoria, 'ilustracao':'pepsi de garrafa.jpg'},
               {'nome':'Pepsi latinha' , 'valor':5.50, 'subcategoria':subcategoria, 'ilustracao':'pepsi lata2.jpg'},
               {'nome':'Coquetel 400ml' , 'valor':10.00, 'subcategoria':subcategoria, 'ilustracao':'coqueteis3.jpg'},
               {'nome':'Coquetel 550ml' , 'valor':14.50, 'subcategoria':subcategoria, 'ilustracao':'coqueteis2.jpg'},
               {'nome':'Coquetel 700ml' , 'valor':17.00, 'subcategoria':subcategoria, 'ilustracao':'coqueteis1.jpg'},
               {'nome':'Suco de Goiaba' , 'valor':3.00, 'subcategoria':subcategoria, 'ilustracao':'suco de goiaba.jpg'},
               {'nome':'Suco de Laranja' , 'valor':3.00, 'subcategoria':subcategoria, 'ilustracao':'suco de laranja.jpg'},
               {'nome':'Suco de Maracujá' , 'valor':3.00, 'subcategoria':subcategoria,'ilustracao':'suco de maracujá.jpg'},
               ]
    produtos =[{'nome':'Caldo de Camarão' , 'valor':45.30, 'subcategoria':subcategoria,'ilustracao':'caldo de camarão.jpg'}, 
               {'nome':'Vaca atoalada' , 'valor':75.00, 'subcategoria':subcategoria,'ilustracao':'vaca atolada.jpg'},
               {'nome':'Galinha Capoeira' , 'valor':25.99, 'subcategoria':subcategoria,'ilustracao':'galinha de capoeira.jpg'},
               {'nome':'Lasanha' , 'valor':35.00, 'subcategoria':subcategoria,'ilustracao':'lasanha.jpg'},
               {'nome':'Macarrão' , 'valor':19.90, 'subcategoria':subcategoria,'ilustracao':'macarrão.jpg'},
               {'nome':'cuscuz' , 'valor':12.00, 'subcategoria':subcategoria,'ilustracao':'cuscuz.jpg'},
               {'nome':'Pirão' , 'valor':23.70, 'subcategoria':subcategoria,'ilustracao':'pirão.jpg'},
               {'nome':'Picanha' , 'valor':70.99, 'subcategoria':subcategoria,'ilustracao':'picanha.jpg'},
               {'nome':'Arroz temperado' , 'valor':10.00, 'subcategoria':subcategoria,'ilustracao':'arroz temperado.jpg'},
               {'nome':'Arroz puro' , 'valor':6.70, 'subcategoria':subcategoria,'ilustracao':'arroz puro.jpg'}
               ]'''
    produtos =[
        {'nome':'Tigela de Sorvete' , 'valor':7.0, 'subcategoria':subcategoria,'ilustracao':'sorvete.jpg'},
        {'nome':'Sorvete com brownie' , 'valor':15.50, 'subcategoria':subcategoria,'ilustracao':'sorvete com brownie.jpg'},
        {'nome':'Pudim' , 'valor':8.00, 'subcategoria':subcategoria,'ilustracao':'pudim.jpg'},
        {'nome':'Mine bolinho' , 'valor':14.00, 'subcategoria':subcategoria,'ilustracao':'mine bolinho.jpg'},
        {'nome':'Pavê(por pedaço)' , 'valor':6.50, 'subcategoria':subcategoria,'ilustracao':'pavê.jpg'},
        {'nome':'Pavê(inteiro)' , 'valor':40.00, 'subcategoria':subcategoria,'ilustracao':'pavê.jpg'}
        ]
    
    for produto in produtos:
        novo_produto = Produto(nome=produto['nome'], valor=produto['valor'], subcategoria=produto['subcategoria'], ilustracao = produto['ilustracao'])
        db.session.add(novo_produto) 
        print("O produto", produto['nome'], "foi adicionado com sucesso")
    db.session.commit()

    
    '''usuario = db.session.query(Usuario).filter_by(id=2).first()
    vinho = db.session.query(Produto).filter_by(id=10).first()
    batata = db.session.query(Produto).filter_by(id=3).first()
    hamburguer = db.session.query(Produto).filter_by(id=5).first()

    # Criar um novo pedido
    novo_pedido = Pedido(
        usuario_id=usuario.id,
        total=vinho.valor + batata.valor * 2 + hamburguer.valor * 3
    )

    # Adicionar itens ao pedido
    itens = [
        {'produto': vinho, 'quantidade': 1},
        {'produto': batata, 'quantidade': 2},
        {'produto': hamburguer, 'quantidade': 3}
    ]   

    for item in itens:
        novo_item = ItemPedido(
            produto_id=item['produto'].id,
            quantidade=item['quantidade'],
            preco_unitario=item['produto'].valor
        )
        novo_pedido.itens.append(novo_item)

    db.session.add(novo_pedido)
    db.session.commit()'''