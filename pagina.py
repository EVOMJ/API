from flask import Flask


# app = Flask(__name__)


# 1.nomes/idade rota de INPUT
# @app.route('/')
# def home():
#     nome = "João"
#     idade = 30
#     return(f"{nome} e {idade}")


# if __name__ == "__main__":
#     app.run(debug=True)



# app = Flask(__name__)


# # 1.nomes/idade rota de INPUT
# @app.route('/<nome>')
# def home(nome):
#     return "{}".format(nome)


# if __name__ == "__main__":
#     app.run(debug=True)


# 2 - Criem uma rota para Calculadora:
## SOMA
## SUBTRAÇÃO
## DIVISÃO
## MULTIPLICAÇÃO

app = Flask(__name__)

@app.route("/")
def usuario():
    return 'Usuario'

@app.route('/calculo/soma')
def soma():

    return "{}".format(soma)




if __name__ == "__main__":
    app.run(debug=True)










