from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def homekkj():
    return render_template("index.html")

@app.route("/desconhecido")
def pagina_desconhecido():
    return render_template("desconhecido.html")

@app.route("/contato")
def pagina_contato():
    return render_template("contato.html")

@app.route("/produtos")
def pagina_produtos():
    lista_produtos = [
        {"nome": "tapioca", "descricao": "inves de farinha, cocaina"},
        {"nome": "feijão", "descricao": "hmmmmm feijãozim"},
        {"nome": "batata", "descricao": "nunca te esqueceremos sasha"}
    ]
    return render_template("produtos.html", produtos = lista_produtos)