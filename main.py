from flask import Flask, render_template, request, redirect

app = Flask(__name__) #instancia o flask no aplicativo
contatos = []
consulta = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)


@app.route('/inserir_contato')
def inserir_contato():
    return render_template('adicionarcontato.html')


@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        pet = request.form['pet']
        especie = request.form['especie']
        email = request.form['email']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nome, pet, especie, email, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_contato.html')  # Renderiza o formulário de adicionar contato

@app.route('/modificar')
def modificar():
    return render_template('edicao_cadastro.html')

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
    del contatos[codigo]
    return redirect('/')



@app.route('/calculosoro')
def calculosoro():
    return render_template('calculosoro.html')

@app.route('/calcular_soro', methods=['GET', 'POST'])
def calcular_soro():

    peso = float(request.form['peso'])
    grau_de_desidratação = request.form['grau']

    if request.method == ['POST']:
        if grau_de_desidratação == 'leve':
            fluido = 50
        elif grau_de_desidratação == 'moderada':
            fluido = 75
        elif grau_de_desidratação == 'grave':
            fluido = 100
        resultado = peso * fluido
        return render_template('calculosoro.html',resultado=resultado)


@app.route('/calcular_medicamento')
def calcular_medicamento():
    return render_template('calculomedicamento.html')

@app.route('/medicamento', methods=['GET', 'POST'])
def medicamento():

    if request.method == ['POST']:
        peso = float(request.form['peso'])
        dose = float(request.form['dose'])
        resultado = peso * dose
        return render_template('calculomedicamento.html', resultado=resultado)

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/inserir_agendamento', methods=['GET', 'POST'])
def inserir_agendamento():

    if request.method == ['POST']:
        nm_animal = request.form['nome_animal']
        nm_tutor = request.form['nome_tutor']
        data = request.form['data']
        horario = request.form['horario']
        sintomas = request.form['sintomas']
        codigo = len(consulta)
        consulta.append = ([codigo, nm_animal, nm_tutor, data, horario, sintomas])

        return render_template('agendamento.hmtl', consulta=consulta)

@app.route('/caes')
def caes():
    return render_template('calculadoracaes.html')

@app.route('/calculadora_caes', methods=['GET', 'POST'])
def calculadora_caes():

    if request.method == ['POST']:
        idade_dog = int(request.form['idade_dog'])
        idade_humano = 0

        if idade_dog == 1:
            idade_humano = idade_dog * 15
        elif idade_dog <= 7:
            idade_humano = 24 + (idade_dog - 2) * 4
        else:
            idade_humano = 44 + (idade_dog - 7) * 5

        return render_template('calculadoracaes.html', idade_humano = idade_humano)

@app.route('/gatos')
def gatos():
    return render_template('calculadoragatos.html')

@app.route('/calculadora_gatos', methods=['GET', 'POST'])
def calculadora_gatos():
    if request.method == ['POST']:
        idade_cat = int(request.form['idade_cat'])
        idade_humano = 0

        if idade_cat <= 2:
            idade_humano = idade_cat * 15
        elif idade_cat <= 7:
            idade_humano = 24 + (idade_cat - 2) * 4
        else:
            idade_humano = 44 + (idade_cat - 7) * 4

        return render_template('calculadoragatos.html', idade_humano=idade_humano)

if __name__ == '__main__':
    app.run(debug=True)