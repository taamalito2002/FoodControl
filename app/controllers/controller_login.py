from flask import Blueprint, render_template, request, redirect, url_for, flash, session

login_bp = Blueprint('login', __name__)

# Base de datos simple en memoria
users_db = {}  # { "usuario": "password" }


# LOGIN
@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users_db and users_db[username] == password:
            session['user_id'] = username
            session['username'] = username
            flash("Bienvenido!", "success")
            return redirect(url_for('dashboard.dashboard'))

        flash("Usuario o contrasena incorrectos", "error")
        return redirect(url_for('login.login'))

    return render_template('login.html')


# REGISTRO
@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users_db:
            flash("El usuario ya existe", "error")
            return redirect(url_for('login.register'))

        users_db[username] = password
        flash("Usuario registrado con exito", "success")
        return redirect(url_for('login.login'))

    return render_template('register.html')


# RECUPERAR CONTRASENA
@login_bp.route('/recover', methods=['GET', 'POST'])
def recover_password():
    if request.method == 'POST':
        flash("Si el correo esta registrado, recibiras instrucciones.", "info")
        return redirect(url_for('login.login'))

    return render_template('recover.html')

