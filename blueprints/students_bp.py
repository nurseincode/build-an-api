from flask import Blueprint

students_bp = Blueprint('students', __name__)

# Read all - GET /students

# Read one - GET /students/<int:id>

# Create - POST /students

# Update - PUT /students/<int:id>

# Delete - DELETE /students/<int:id>


# Possible extra routes:
# Enrol - POST /students/<int:student_id>/<int:course_id>
# Unenrol - DELETE /students/<int:student_id>/<int:course_id>