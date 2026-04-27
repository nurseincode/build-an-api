from init import db, ma

class Course(db.Model):
    __tablename__= 'courses'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date', 'teacher_id')
        

one_course = CourseSchema()
many_courses = CourseSchema(many=True)

course_without_id = CourseSchema(exclude=['id'])