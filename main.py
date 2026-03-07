from flask import Flask
from init import db, ma 
import os
from blueprints.cli_bp import cli_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

    
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(cli_bp)

    return app