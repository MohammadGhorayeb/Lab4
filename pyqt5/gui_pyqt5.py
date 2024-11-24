import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QTableWidget, 
                             QTableWidgetItem, QHeaderView, QMessageBox, 
                             QFileDialog, QInputDialog)
from PyQt5.QtCore import Qt
from models import Student, Instructor, Course
import json

# Dummy data lists
students = []
instructors = []
courses = []
# Main application window
class SchoolManagementSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Management System")
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()

        # Tabs to switch between different sections
        self.add_student_layout()
        self.add_instructor_layout()
        self.add_course_layout()
        self.view_records_layout()
        self.search_records_layout()
        self.add_actions_layout()


        self.setLayout(self.layout)

    # Add student form
    def add_student_layout(self):
        layout = QHBoxLayout()

        # Form labels and inputs
        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.student_id_input = QLineEdit(self)

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel("Student ID:"))
        layout.addWidget(self.student_id_input)

        # Add student button
        add_student_btn = QPushButton("Add Student")
        add_student_btn.clicked.connect(self.add_student)
        layout.addWidget(add_student_btn)

        self.layout.addLayout(layout)

    # Add instructor form
    def add_instructor_layout(self):
        layout = QHBoxLayout()

        self.instructor_name_input = QLineEdit(self)
        self.instructor_age_input = QLineEdit(self)
        self.instructor_email_input = QLineEdit(self)
        self.instructor_id_input = QLineEdit(self)

        layout.addWidget(QLabel("Instructor Name:"))
        layout.addWidget(self.instructor_name_input)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.instructor_age_input)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.instructor_email_input)
        layout.addWidget(QLabel("Instructor ID:"))
        layout.addWidget(self.instructor_id_input)

        add_instructor_btn = QPushButton("Add Instructor")
        add_instructor_btn.clicked.connect(self.add_instructor)
        layout.addWidget(add_instructor_btn)

        self.layout.addLayout(layout)

    # Add course form
    def add_course_layout(self):
        layout = QHBoxLayout()

        self.course_id_input = QLineEdit(self)
        self.course_name_input = QLineEdit(self)

        layout.addWidget(QLabel("Course ID:"))
        layout.addWidget(self.course_id_input)
        layout.addWidget(QLabel("Course Name:"))
        layout.addWidget(self.course_name_input)

        add_course_btn = QPushButton("Add Course")
        add_course_btn.clicked.connect(self.add_course)
        layout.addWidget(add_course_btn)

        self.layout.addLayout(layout)

    # Table to display records (students, instructors, courses)
    def view_records_layout(self):
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Type", "Details"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        refresh_btn = QPushButton("Refresh Records")
        refresh_btn.clicked.connect(self.update_table)

        self.layout.addWidget(self.table)
        self.layout.addWidget(refresh_btn)

    # Search form
    def search_records_layout(self):
        layout = QHBoxLayout()

        self.search_input = QLineEdit(self)
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search)

        layout.addWidget(QLabel("Search by Name or ID:"))
        layout.addWidget(self.search_input)
        layout.addWidget(search_btn)

        self.layout.addLayout(layout)

    # Add student function
    def add_student(self):
        name = self.name_input.text()
        age = self.age_input.text()
        email = self.email_input.text()
        student_id = self.student_id_input.text()

        if name and age.isdigit() and email and student_id:
            student = Student(name, int(age), email, student_id)
            students.append(student)
            QMessageBox.information(self, "Success", "Student added successfully")
        else:
            QMessageBox.warning(self, "Error", "Invalid input")

    # Add instructor function
    def add_instructor(self):
        name = self.instructor_name_input.text()
        age = self.instructor_age_input.text()
        email = self.instructor_email_input.text()
        instructor_id = self.instructor_id_input.text()

        if name and age.isdigit() and email and instructor_id:
            instructor = Instructor(name, int(age), email, instructor_id)
            instructors.append(instructor)
            QMessageBox.information(self, "Success", "Instructor added successfully")
        else:
            QMessageBox.warning(self, "Error", "Invalid input")

    # Add course function
    def add_course(self):
        course_id = self.course_id_input.text()
        course_name = self.course_name_input.text()

        if course_id and course_name:
            course = Course(course_id, course_name)
            courses.append(course)
            QMessageBox.information(self, "Success", "Course added successfully")
        else:
            QMessageBox.warning(self, "Error", "Invalid input")

    # Update table with records
    def update_table(self):
        self.table.setRowCount(0)
        for student in students:
            self.add_table_row(student.student_id, student.name, "Student", f"Courses: {len(student.registered_courses)}")
        for instructor in instructors:
            self.add_table_row(instructor.instructor_id, instructor.name, "Instructor", f"Courses: {len(instructor.assigned_courses)}")
        for course in courses:
            instructor_name = course.instructor.name if course.instructor else "None"
            self.add_table_row(course.course_id, course.course_name, "Course", f"Students: {len(course.enrolled_students)}, Instructor: {instructor_name}")

    # Add a row to the table
    def add_table_row(self, id, name, type, details):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(id))
        self.table.setItem(row_position, 1, QTableWidgetItem(name))
        self.table.setItem(row_position, 2, QTableWidgetItem(type))
        self.table.setItem(row_position, 3, QTableWidgetItem(details))

    # Search functionality
    def search(self):
        query = self.search_input.text().lower()
        self.table.setRowCount(0)  # Clear current table

        # Search students
        for student in students:
            if query in student.name.lower() or query in student.student_id.lower():
                self.add_table_row(student.student_id, student.name, "Student", f"Courses: {len(student.registered_courses)}")

        # Search instructors
        for instructor in instructors:
            if query in instructor.name.lower() or query in instructor.instructor_id.lower():
                self.add_table_row(instructor.instructor_id, instructor.name, "Instructor", f"Courses: {len(instructor.assigned_courses)}")

        # Search courses
        for course in courses:
            if query in course.course_id.lower() or query in course.course_name.lower():
                instructor_name = course.instructor.name if course.instructor else "None"
                self.add_table_row(course.course_id, course.course_name, "Course", f"Students: {len(course.enrolled_students)}, Instructor: {instructor_name}")

    
    def add_actions_layout(self):
        layout = QHBoxLayout()

        # Add Edit button
        edit_btn = QPushButton("Edit Record")
        edit_btn.clicked.connect(self.edit_record)
        layout.addWidget(edit_btn)

        # Add Delete button
        delete_btn = QPushButton("Delete Record")
        delete_btn.clicked.connect(self.delete_record)
        layout.addWidget(delete_btn)

        # Add Save button
        save_btn = QPushButton("Save Data")
        save_btn.clicked.connect(self.save_data)
        layout.addWidget(save_btn)

        # Add Load button
        load_btn = QPushButton("Load Data")
        load_btn.clicked.connect(self.load_data)
        layout.addWidget(load_btn)

        self.layout.addLayout(layout)


    def edit_record(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "No record selected")
            return

        record_type = self.table.item(selected_row, 2).text()  # Type (Student/Instructor/Course)
        record_id = self.table.item(selected_row, 0).text()  # ID

        if record_type == "Student":
            student = next((s for s in students if s.student_id == record_id), None)
            if student:
                new_name, ok = self.get_input("Edit Student", "Name", student.name)
                if ok:
                    student.name = new_name
                new_age, ok = self.get_input("Edit Student", "Age", student.age)
                if ok:
                    student.age = int(new_age)
                new_email, ok = self.get_input("Edit Student", "Email", student._email)
                if ok:
                    student._email = new_email
        elif record_type == "Instructor":
            instructor = next((i for i in instructors if i.instructor_id == record_id), None)
            if instructor:
                new_name, ok = self.get_input("Edit Instructor", "Name", instructor.name)
                if ok:
                    instructor.name = new_name
                new_age, ok = self.get_input("Edit Instructor", "Age", instructor.age)
                if ok:
                    instructor.age = int(new_age)
                new_email, ok = self.get_input("Edit Instructor", "Email", instructor._email)
                if ok:
                    instructor._email = new_email
        elif record_type == "Course":
            course = next((c for c in courses if c.course_id == record_id), None)
            if course:
                new_name, ok = self.get_input("Edit Course", "Course Name", course.course_name)
                if ok:
                    course.course_name = new_name

        self.update_table()

    def get_input(self, title, field, value):
        text, ok = QInputDialog.getText(self, title, f"Edit {field}:", QLineEdit.Normal, str(value))
        return text, ok


    def delete_record(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "No record selected")
            return

        record_type = self.table.item(selected_row, 2).text()
        record_id = self.table.item(selected_row, 0).text()

        if record_type == "Student":
            student = next((s for s in students if s.student_id == record_id), None)
            if student:
                students.remove(student)
        elif record_type == "Instructor":
            instructor = next((i for i in instructors if i.instructor_id == record_id), None)
            if instructor:
                instructors.remove(instructor)
        elif record_type == "Course":
            course = next((c for c in courses if c.course_id == record_id), None)
            if course:
                courses.remove(course)

        self.update_table()
        QMessageBox.information(self, "Success", "Record deleted successfully")

    def save_data(self):
        data = {
            "students": [{"name": s.name, "age": s.age, "email": s._email, "id": s.student_id} for s in students],
            "instructors": [{"name": i.name, "age": i.age, "email": i._email, "id": i.instructor_id} for i in instructors],
            "courses": [{"id": c.course_id, "name": c.course_name, "students": [s.student_id for s in c.enrolled_students]} for c in courses]
        }

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "JSON Files (*.json)", options=options)
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            QMessageBox.information(self, "Success", "Data saved successfully")

    def load_data(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Data", "", "JSON Files (*.json)", options=options)
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)

            students.clear()
            instructors.clear()
            courses.clear()

            # Rebuild the data from the JSON file
            for student_data in data['students']:
                student = Student(student_data['name'], student_data['age'], student_data['email'], student_data['id'])
                students.append(student)

            for instructor_data in data['instructors']:
                instructor = Instructor(instructor_data['name'], instructor_data['age'], instructor_data['email'], instructor_data['id'])
                instructors.append(instructor)

            for course_data in data['courses']:
                course = Course(course_data['id'], course_data['name'])
                courses.append(course)

                # Link students to the course
                for student_id in course_data['students']:
                    student = next((s for s in students if s.student_id == student_id), None)
                    if student:
                        course.add_student(student)

            self.update_table()
            QMessageBox.information(self, "Success", "Data loaded successfully")
