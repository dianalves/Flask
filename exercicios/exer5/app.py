from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='public')

#Metodos HTTP, GET,POST

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        return dumps(request.form)
    return 'OK GET'

if __name__ == '__main__':
    app.run(debug=True,)