from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/produtos")
def page_produtos():

    lista_produtos = [
        {"nome": "Coca-Cola", "descricao": "Mata a sede e você"},
        {"nome": "Molho de Tomate", "descricao": "Queremos acreditar que tudo aquilo é apenas tomate"},
        {"nome": "Chocolate", "descricao": "Bueno"}
    ]

    return render_template("produtos.html", lista_produtos = lista_produtos)

@app.route("/contato", methods=['GET', 'POST'])
def page_contato():

    cpf = CPF()
    cnpj = CNPJ()
    cpf_site = cpf.generate(True)
    cnpj_site = cnpj.generate(True)

    if request.method == 'GET':
        return render_template("contato.html", cpf = cpf_site, cnpj = cnpj_site)
    else:
        return render_template("contato.html", cpf = cpf_site, cnpj = cnpj_site)

@app.route("/termos_de_uso")
def page_termos_de_uso():
    return render_template("termos_de_uso.html")

@app.route("/politica_privacidade")
def page_politica_privacidade():
    return render_template("politica_privacidade.html")

@app.route("/como_utilizar")
def page_como_utilizar():
    return render_template("como_utilizar.html")

if __name__ == '__main__':
    app.run(debug=True)