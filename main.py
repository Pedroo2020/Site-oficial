from flask import Flask, render_template, request, redirect
app = Flask(__name__) #instancia o flask no aplicativo

#lista
contatos = []


@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)


@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        pet = request.form['pet']
        especie = request.form['especie']
        email = request.form['email']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nome, pet, especie, email, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_contato.html')


if __name__ == '__main__':
    app.run(debug=True) #executa o aplicativo Flask