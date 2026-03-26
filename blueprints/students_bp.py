from flask import Blueprint
from init import db
from models.student import Student, many_students

students_bp = Blueprint('students', __name__)

# Read all - GET /students
@students_bp.route('/students')
def get_all_students():
    stmt = db.select(Student)
    students = db.session.scalars(stmt)
    return many_students.dump(students)


# Read one - GET /students/<int:id>
@students_bp.route('/students/<int:student_id>')
def get_one_student(student_id):
    stmt = db.select(Student).filter_by(id=student_id)
    student = db.session.scalar(stmt)

# Create - POST /students

# Update - PUT /students/<int:id>

# Delete - DELETE /students/<int:id>


# Possible extra routes:
# Enrol - POST /students/<int:student_id>/<int:course_id>
# Unenrol - DELETE /students/<int:student_id>/<int:course_id>