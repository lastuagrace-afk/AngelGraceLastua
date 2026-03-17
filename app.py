from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/yourdatabase'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{ 'id': student.id, 'name': student.name, 'age': student.age } for student in students])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added'}), 201

if __name__ == '__main__':
    app.run(debug=True)