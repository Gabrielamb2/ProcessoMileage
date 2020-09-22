from flask import Flask, jsonify, request, render_template, redirect
from flask import url_for

app = Flask(__name__)

carros = [
    {
        'modelo': 'Fusca',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1982',
        'preco': '15.000'
    },

    {
        'modelo': 'Monza',
        'motor': '1.6',
        'marca': 'Chevrolet',
        'ano': '1982',
        'preco': '10.000'
    },

    {
        'modelo': 'Mustang GT',
        'motor': '390 V8',
        'marca': 'Ford',
        'ano': '1966',
        'preco': '150.000'
    },
    {
        'modelo': 'Chevette',
        'motor': '1.6',
        'marca': 'Chevrolet',
        'ano': '1987',
        'preco': '10.000'

    },

    {
        'modelo': 'Gol',
        'motor': '1.8',
        'marca': 'Volkswagen',
        'ano': '1988',
        'preco': '25.000'
    },
    {
        'modelo': 'Uno Mille',
        'motor': '1.5',
        'marca': 'Fiat',
        'ano': '1984',
        'preco': '20.000'
    },
    {
        'modelo': 'Passat',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1982',
        'preco': '10.000'
    },

    {
        'modelo': 'Opala',
        'motor': '2.5',
        'marca': 'Chevrolet',
        'ano': '1981',
        'preco': '15.000'
    },

    {
        'modelo': 'Maverick',
        'motor': '4.9 V8',
        'marca': 'Ford',
        'ano': '1976',
        'preco': '60.000'
    },
    {
        'modelo': 'Kadett',
        'motor': '1.8',
        'marca': 'Chevrolet',
        'ano': '1989',
        'preco': '15.000'
    },

    {
        'modelo': 'Kombi',
        'motor': '1.4',
        'marca': 'Volkswagen',
        'ano': ' 1957',
        'preco': '25.000'
    },


    {
        'modelo': 'Santana',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1984',
        'preco': '10.000'
    },





]


# INSIRA SEU CÓDIGO! BOA SORTE :)


# Acessar a informação de todos os carros

# @app.route('/', methods=['GET'])
# def api_all():
#     return jsonify({'carros': carros})

@app.route('/index')
def principal():
    return render_template("Principal.html", carros = carros[:])


# Filtrar os carros de acordo com as especificações do cliente (motor e ano).

@app.route('/filtrar/<string:motor>/<string:ano>/<string:marca>', methods=['GET'])
def return_one(motor,ano,marca):
    filtragem=[]
    i=0
    for carro in carros:
        if carro['motor']==motor and carro['ano']==ano and carro['marca']==marca:
             return render_template("filtrado.html", carros = carro)
        i+=1
    return render_template("filtrar_modelo.html", carros = carros)



@app.route('/filtrar', methods=["GET","POST"])
def flitrar():
    if request.method == "POST":
        motor = request.form["motor"]
        ano =  request.form["ano"]
        marca = request.form["marca"]
        return redirect(url_for("return_one", motor = motor, ano = ano,marca=marca))
    else:
        return render_template("filtrar_modelo.html", carros = carros[:])

#Adicionar um novo modelo ao dicionário

@app.route('/add', methods=["GET","POST"])
def addOne():
    if request.method == "POST":
        modelo = request.form["modelo"]
        motor = request.form["motor"]
        ano =  request.form["ano"]
        marca = request.form["marca"]
        preco = request.form["preco"]

        carro = {'modelo': modelo,'motor': motor,'marca': marca,'ano':ano,'preco': preco }
        carros.append(carro)
        return render_template("adicionar_modelo.html", carros = carros[:])
    else:
        return render_template("adicionar_modelo.html", carros = carros[:])
   


#Alterar o motor de algum dos modelos

@app.route('/alterar/<string:modelo>/<string:motor>', methods=["PUT","GET"])
def editOne(modelo,motor):
     for carro in carros:
        if carro['modelo']==modelo:
            carro['motor']=motor
            return render_template("alterar_modelo.html", carros = carros[:])
    # car = [carro for carro in carros if carro['motor']==muda]
    # car[0]['motor'] = request.json['motor']
    # return jsonify({'carros': car[0]})

@app.route('/alterar', methods=["GET","POST"])
def alterar():
    if request.method == "POST":
        modelo = request.form["modelo"]
        motor = request.form["motor"]
        return redirect(url_for("editOne",modelo = modelo, motor = motor))
            
    else:
        return render_template("alterar_modelo.html", carros = carros[:])


#Deletar um dos modelos.

@app.route('/deletar/<string:modelo>', methods=["DELETE","GET"])
def removeOne(modelo):
    carrinho = []
    for carro in carros:
        if carro['modelo']==modelo:
            print("piii")
            print(carro['modelo'])
            carros.remove(carro)
            return render_template("remover_modelo.html", carros = carros)
    if carrinho == []:
        return f"<h1>Deu ruim</h1>"
    




@app.route('/delet',methods=["GET","POST"])
def delet():
    if request.method == "POST":
        modelo = request.form["modelo"]
        return redirect(url_for("removeOne",modelo=modelo))
    else:
        return render_template("remover_modelo.html", carros = carros[:])


    # text = request.form('u')
    # car = [carro for carro in carros if carro['modelo']==text]
    # carros.remove(car[0])
    # return render_template("remover_modelo.html", carros = carros[:])




if __name__ == '__main__':
    app.run(debug=True)
