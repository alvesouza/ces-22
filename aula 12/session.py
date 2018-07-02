from flask import Flask, render_template, request, redirect
app = Flask(__name__)

session = {}
# session['username'] = 'admin'
# session.pop('username', None)


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Log com o seu nome de usuario ' + username + '<br>' + "<b><a href = '/logout'>clique aqui para sair</a></b>"
    return "Você não está logado <br><a href = '/login'></b>clique aqui para logar</b></a>"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return '<h1>Bem vindo ' + session['username'] + '!</h1>'+ "<b><a href = '/logout'>clique aqui para sair</a></b>"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug = True)