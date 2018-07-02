from flask import Flask, render_template, request, make_response
app = Flask(__name__)

session = {}

def checar_professor(nome):
    minimo = nome.lower()
    if minimo == 'yano':
        return True
    return False

@app.route('/')
def index():
    return render_template('ID.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nome']

    resposta = make_response(render_template('cookies.html'))
    resposta.set_cookie('userID', user)

    return resposta


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    if (checar_professor(name)):
        return '<h1>Olá professor ' + name + '!</h1>'
    return '<h1>O cookie é "'+name+'"!</h1>'


if __name__ == '__main__':
    app.run(debug = True)