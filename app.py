from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página "Sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para a página "Filtros"
@app.route('/filtros')
def filtros():
    return render_template('filtros.html')

# Rota para a página "Contato"
@app.route('/contatos')
def contato():
    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(debug=True)
