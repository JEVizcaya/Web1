from flask import Flask, render_template, request,redirect, url_for,session

app = Flask(__name__)
app.secret_key='123456'

@app.route('/login', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<int:edad>')
def saludo(nombre,edad):
    if edad < 18:
        return f'Hola, {nombre} Eres menor de edad.'
    else:
        
        return f'Hola, {nombre} Eres mayor de edad.'
    
#login post

@app.route('/login', methods=['POST'])
def login():
   #obtener datos formulario
    username = request.form['username']
    password = request.form['password']
    if (username == 'admin' and password == 'admin'):
        #guardar en sesion
        session['username'] = username
        
        return redirect(url_for('admin'))
    else:
    
        return render_template('index.html', error='Usuario o contraseña incorrectos')

@app.route('/admin', methods=['GET'])
def admin():
    if 'username' in session:
        return render_template('admin/admin.html')
    else:
        return redirect(url_for('login'))
   

if __name__ == '__main__':
    app.run(debug=True,port=80)
