from flask import Flask, redirect, url_for
#colocando instancia do flask em uma variavel
app = Flask(__name__)

#criando rotas
@app.route('/')
def index():
    return 'Index'


@app.route('/teste')
def teste():
    return 'teste'


#criando URL dinâmica
@app.route('/hello')
@app.route('/hello/<nome>')
def hello(nome=''):
    return "<h1>Hello {}</h1>".format(nome)


@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID=-1):
    if postID >= 0:
        return 'blog info {}'.format(postID)
    else:
        return 'Blog todo'


#construção URL com redirecionamento
@app.route('/admin')
def admin():
    return '<h1>Admin</h1>'


@app.route('/guest/<name>')
def guest(name):
    return '<p>Ola guest <b>{}<b></p>'.format(name)


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name=name))


@app.route('/google')
def google():
    return redirect('http://google.com')


#ativando debug para careegar automaticamente
if __name__ == '__main__':
    app.run(debug=True, port='5000')