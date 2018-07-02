from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        arquivo = str(request.form['archive'])
        if arquivo != '':
            return render_template(arquivo + '.html')
        else:
            return render_template('arquivos.html')
    else:
        return render_template('arquivos.html')

if __name__ == '__main__':
    app.run(debug = True)