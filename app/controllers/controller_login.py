from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.authenticate(username, password):
            session['user'] = username  # Guardar usuario en la sesión
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('login.dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')


@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.register(username, password):
            flash('Usuario registrado correctamente', 'success')
            return redirect(url_for('login.login'))
        else:
            flash('El usuario ya existe', 'error')
    return render_template('register.html')


@login_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Debes iniciar sesión primero', 'error')
        return redirect(url_for('login.login'))
    return render_template('dashboard.html')


@login_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('login.login'))
