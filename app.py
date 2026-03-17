from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Juan", "grade": 85, "section": "Zechariah"},
    {"id": 2, "name": "Maria", "grade": 90, "section": "Zechariah"},
    {"id": 3, "name": "Pedro", "grade": 70, "section": "Zion"}
]

# Home
@app.route('/')
def home():
    return redirect(url_for('list_students'))

# -------------------------------
# VIEW STUDENTS (ENHANCED UI)
# -------------------------------
@app.route('/students')
def list_students():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Manager</title>
        <!-- Bootstrap 5 CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- FontAwesome Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            body { background-color: #f4f6f9; }
            .navbar { box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .card { border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .table thead th { background-color: #0d6efd; color: white; border: none; }
            .table tbody tr:hover { background-color: #e9ecef; }
            .btn-action { margin-right: 5px; }
        </style>
    </head>
    <body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="fas fa-user-graduate me-2"></i>Student Manager
            </a>
            <div class="d-flex">
                <a href="/api/students" class="btn btn-outline-light btn-sm" target="_blank">
                    <i class="fas fa-code me-1"></i>View API
                </a>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h3 class="text-muted">Student Records</h3>
            <a href="/add_student_form" class="btn btn-success">
                <i class="fas fa-plus-circle me-1"></i> Add Student
            </a>
        </div>

        <div class="card">
            <div class="card-body p-0">
                <div class="table-responsive">
                    <table class="table table-hover mb-0">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Grade</th>
                                <th>Section</th>
                                <th class="text-center">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        {% for s in students %}
                        <tr>
                            <td><span class="badge bg-secondary">{{s.id}}</span></td>
                            <td><strong>{{s.name}}</strong></td>
                            <td>{{s.grade}}</td>
                            <td>{{s.section}}</td>
                            <td class="text-center">
                                <a href="/edit_student/{{s.id}}" class="btn btn-sm btn-warning btn-action" title="Edit">
                                    <i class="fas fa-edit"></i> Edit
                                </a>
                                <a href="/delete_student/{{s.id}}" class="btn btn-sm btn-danger btn-action" 
                                   onclick="return confirm('Are you sure you want to delete {{s.name}}?')" title="Delete">
                                    <i class="fas fa-trash-alt"></i> Delete
                                </a>
                            </td>
                        </tr>
                        {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <footer class="text-center text-muted mt-5 mb-3">
        </footer>
    </div>

    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(html, students=students)

# -------------------------------
# ADD STUDENT FORM (ENHANCED UI)
# -------------------------------
@app.route('/add_student_form')
def add_student_form():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add Student</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            body { background-color: #f4f6f9; }
            .form-card { 
                max-width: 500px; 
                margin: auto; 
                border: none; 
                box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                border-radius: 10px;
            }
            .card-header { background-color: #198754; color: white; border-radius: 10px 10px 0 0 !important; }
        </style>
    </head>
    <body class="py-5">

        <div class="container">
            <div class="card form-card">
                <div class="card-header text-center py-3">
                    <h4 class="mb-0"><i class="fas fa-user-plus me-2"></i>New Student</h4>
                </div>
                <div class="card-body p-4">
                    <form method="POST" action="/add_student">
                        <div class="mb-3">
                            <label class="form-label">Full Name</label>
                            <input type="text" name="name" class="form-control" placeholder="Enter name" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Grade</label>
                            <input type="number" name="grade" class="form-control" placeholder="e.g. 85" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Section</label>
                            <input type="text" name="section" class="form-control" placeholder="e.g. Zion" required>
                        </div>
                        <div class="d-grid mt-4">
                            <button type="submit" class="btn btn-success">
                                <i class="fas fa-save me-1"></i> Save Student
                            </button>
                        </div>
                    </form>
                </div>
                <div class="card-footer text-center text-muted bg-white border-0 pb-3">
                    <a href="/students" class="text-decoration-none"><i class="fas fa-arrow-left me-1"></i> Back to List</a>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(html)

# -------------------------------
# ADD STUDENT LOGIC
# -------------------------------
@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        name = request.form.get("name")
        grade = int(request.form.get("grade"))
        section = request.form.get("section")

        new_student = {
            "id": max([s["id"] for s in students]) + 1 if students else 1,
            "name": name,
            "grade": grade,
            "section": section
        }

        students.append(new_student)
    except Exception as e:
        return f"Error adding student: {e}"

    return redirect(url_for('list_students'))

# -------------------------------
# DELETE STUDENT
# -------------------------------
@app.route('/delete_student/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect(url_for('list_students'))

# -------------------------------
# EDIT STUDENT (ENHANCED UI)
# -------------------------------
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s["id"] == id), None)

    if not student:
        return "Student not found", 404

    if request.method == 'POST':
        student["name"] = request.form["name"]
        student["grade"] = int(request.form["grade"])
        student["section"] = request.form["section"]
        return redirect(url_for('list_students'))

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Student</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            body { background-color: #f4f6f9; }
            .form-card { 
                max-width: 500px; 
                margin: auto; 
                border: none; 
                box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                border-radius: 10px;
            }
            .card-header { background-color: #ffc107; color: #212529; border-radius: 10px 10px 0 0 !important; }
        </style>
    </head>
    <body class="py-5">

        <div class="container">
            <div class="card form-card">
                <div class="card-header text-center py-3">
                    <h4 class="mb-0"><i class="fas fa-user-edit me-2"></i>Edit Student</h4>
                </div>
                <div class="card-body p-4">
                    <form method="POST">
                        <div class="mb-3">
                            <label class="form-label">Full Name</label>
                            <input type="text" name="name" class="form-control" value="{{student.name}}" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Grade</label>
                            <input type="number" name="grade" class="form-control" value="{{student.grade}}" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Section</label>
                            <input type="text" name="section" class="form-control" value="{{student.section}}" required>
                        </div>
                        <div class="d-grid mt-4">
                            <button type="submit" class="btn btn-warning">
                                <i class="fas fa-sync-alt me-1"></i> Update Student
                            </button>
                        </div>
                    </form>
                </div>
                <div class="card-footer text-center text-muted bg-white border-0 pb-3">
                    <a href="/students" class="text-decoration-none"><i class="fas fa-arrow-left me-1"></i> Back to List</a>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(html, student=student)

# -------------------------------
# API
# -------------------------------
@app.route('/api/students')
def api_students():
    return jsonify(students)

# -------------------------------
# RUN
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
