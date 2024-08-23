# API - É um lugar para disponibilizar recursos e funcionalidades 
# Objetivo - Criar um API que disponibiliza a consulta, Criação, edição e exclusao de livros.
# URL base - localhost
# Endpoints -
 #  - localhost/livros (GET)
 #  - localhost/livros/id (GET)
 #  - localhost/livros/id (PUT)
 #  - localhost/livros/id (DELETE)

from flask import Flask, jsonify, request


app1 = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis - A Sociedade do Anel',
        'autor' : 'J.R.R Tolkien'
    },
    {
        'id' : 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id' : 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atómicos'
    },
]

# Consultar (todos) -
@app1.route ('/livros')
def obter_livros():
        return jsonfy(livros)
app1.run(port=5000,host='localhost',debug=True)