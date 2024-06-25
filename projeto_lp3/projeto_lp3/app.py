from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def pagina_produtos():
    lista_produtos = [
        {"nome": "Produto1", "descricao": "Desc"},
        {"nome": "Produto2", "descricao": "Desc"},
        {"nome": "Produto3", "descricao": "Desc"}
    ]
    return render_template("produtos.html", produtos = lista_produtos)

@app.route("/registrar")
def registrar_produtos():
    return render_template("cadastro_produto.html")

