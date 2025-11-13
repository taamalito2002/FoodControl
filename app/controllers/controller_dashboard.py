from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # Verifica si el usuario ha iniciado sesion
    if 'user_id' not in session:
        return redirect(url_for('login.login'))
    
    # Obtiene el nombre del usuario si esta en la sesion
    username = session.get('username', 'Usuario')
    
    return render_template('dashboard.html', username=username)
