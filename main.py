from flask import Flask
from init import db, ma 

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lms_dev:123456@localhost5432/lms_db'
