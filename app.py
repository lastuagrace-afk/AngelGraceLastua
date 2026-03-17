import os
from flask import Flask, jsonify, request, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
# This creates a file named 'students.db' in your project folder
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Student table structure
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(100), nullable=False)

# Automatically create the database file and tables
with app.app_context():
    db.create_all()
# ------------------------------

@app.route('/students')
def list_students():
    # Fetch all students from the database instead of a list
    all_students = Student.query.all()
    # ... (Your existing HTML code here) ...
    return render_template_string(html, students=all_students)

@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        # Create a new Student object
        new_student = Student(
            name=request.form.get("name"),
            grade=int(request.form.get("grade")),
            section=request.form.get("section")
        )
        # Save to database
        db.session.add(new_student)
        db.session.commit()
    except Exception as e:
        return f"Error adding student: {e}"
    return redirect(url_for('list_students'))

@app.route('/delete_student/<int:id>')
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('list_students'))
