from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self. categoria = categoria
        self.console = console


@app.route('/inicio')
def ola_mundo():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Todos')
    jogo2 = Jogo('God of War', 'Hack and Slash', 'PS2')
    jogo3 = Jogo('Elden Ring', 'Souls-like', 'PS5')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

app.run(port=3000)