from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from dotenv import load_dotenv

ALLOWED_CODE = '7966'

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'

def create_database():
    db.create_all()
    print("Database Created")

def create_app():
    # load .env values (SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, FROM_EMAIL, MANAGER_EMAIL, etc.)
    # load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfasl'  # consider moving to env
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import models early so Customer is available for user_loader
    from .models import Customer, Cart, Product, Order

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(int(id))

    # Blueprints
    from .views import views
    from .auth import auth
    from .admin import admin   # <- fixed the dot
    from .cart import cart

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(cart, url_prefix='/')

    with app.app_context():
        create_database()

    return app
