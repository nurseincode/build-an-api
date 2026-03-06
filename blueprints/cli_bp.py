from flask import Blueprint
from init import db

cli_bp = Blueprint('cli_commands', __name__)

@cli_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Tables created')

@cli_bp.cli.comman('seed')
def seed_tables():
