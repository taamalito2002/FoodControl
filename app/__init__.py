from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'H@la'  # Texto, no número

    # Importar rutas
    from app.controllers.controller_login import login_bp
    from app.controllers.controller_dashboard import dashboard_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(dashboard_bp)

    return app
