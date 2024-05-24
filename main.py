from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#lista
contatos = []


@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        codigo = len(contatos)
        contatos.append([codigo, nome, telefone, email])
        return redirect('/')
    else:
        return render_template('adicionar_contato.html')  # Renderiza o formulário de adicionar contato
@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        contatos[codigo] = [codigo, nome, telefone, email]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)  # Renderiza o formulário de edição

@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del contatos[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

if __name__ == '__main__':
    app.run(debug=True) #executa o aplicativo Flask