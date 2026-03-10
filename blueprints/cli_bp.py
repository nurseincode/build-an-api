from flask import Blueprint
from init import db
from models.student import Student

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Tables created')

@cli_bp.cli.command('seed')
def seed_tables():
    students = [
        Student(
            name = 'Mary Jones',
            email = 'mary.jones@gmail.com',
            address = 'Sydney'
        ),
        Student(
            name = 'John Smith',
            email = 'john.smith@outlook.com',
        )
    ]

    db.session.add_all(students)
    db.session.commit()
    print('Tables seeded')

