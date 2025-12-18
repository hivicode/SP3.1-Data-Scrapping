from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/<name>')
# def nama_saya(name):
#     return f'Halo nama saya {name}'

@app.route('/cek_angka/<int:angka>')
def cek_angka(angka):
    if angka % 2 == 0:
        return f'Angka {angka} adalah genap'
    else:
        return f'Angka {angka} adalah ganjil'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        if username == 'test' and password == '123':
            return f'Login berhasil' 
        else:
            return f'Maaf, username atau password salah'
    else:
        return f'Maaf, method tidak diizinkan'

app.run(debug=True)
