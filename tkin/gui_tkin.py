"""
gui_tkin.py

This module contains the GUI implementation for the School Management System using Tkinter.

Classes:
    SchoolManagementSystem:
        Represents the main GUI for managing students, instructors, and courses.

Functions:
    None
"""

import tkinter as tk
from tkinter import ttk, messagebox
from models import Student, Instructor, Course
import json


# Simulated Data Storage
students = []
instructors = []
courses = []

# Tkinter Setup
class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("800x600")
        
        # Create Tabs
        self.tab_control = ttk.Notebook(root)
        self.student_tab = ttk.Frame(self.tab_control)
        self.instructor_tab = ttk.Frame(self.tab_control)
        self.course_tab = ttk.Frame(self.tab_control)
        self.register_tab = ttk.Frame(self.tab_control)
        self.assign_tab = ttk.Frame(self.tab_control)
        self.view_tab = ttk.Frame(self.tab_control)
        self.search_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.student_tab, text="Add Student")
        self.tab_control.add(self.instructor_tab, text="Add Instructor")
        self.tab_control.add(self.course_tab, text="Add Course")
        self.tab_control.add(self.register_tab, text="Register Student to Course")
        self.tab_control.add(self.assign_tab, text="Assign Instructor to Course")
        self.tab_control.add(self.view_tab, text="View Records")
        self.tab_control.add(self.search_tab, text="Search")

        self.tab_control.pack(expand=1, fill="both")

        # Add Save and Load buttons here
        save_button = tk.Button(self.root, text="Save Data", command=self.save_data)
        save_button.pack(side='left', padx=10, pady=10)

        load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        load_button.pack(side='left', padx=10, pady=10)

        # Initialize Components
        self.add_student_form()
        self.add_instructor_form()
        self.add_course_form()
        self.register_student_to_course()
        self.assign_instructor_to_course()
        self.view_records()
        self.search_records()

    # Add Student Form
    def add_student_form(self):
        tk.Label(self.student_tab, text="Student Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.student_tab, text="Age").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.student_tab, text="Email").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.student_tab, text="Student ID").grid(row=3, column=0, padx=10, pady=10)

        self.student_name_entry = tk.Entry(self.student_tab)
        self.student_age_entry = tk.Entry(self.student_tab)
        self.student_email_entry = tk.Entry(self.student_tab)
        self.student_id_entry = tk.Entry(self.student_tab)

        self.student_name_entry.grid(row=0, column=1)
        self.student_age_entry.grid(row=1, column=1)
        self.student_email_entry.grid(row=2, column=1)
        self.student_id_entry.grid(row=3, column=1)

        tk.Button(self.student_tab, text="Add Student", command=self.add_student).grid(row=4, column=1, pady=10)

    def add_student(self):
        name = self.student_name_entry.get()
        age = self.student_age_entry.get()
        email = self.student_email_entry.get()
        student_id = self.student_id_entry.get()

        if name and age.isdigit() and email and student_id:
            try:
                student = Student(name, int(age), email, student_id)
                students.append(student)
                messagebox.showinfo("Success", "Student added successfully")
                self.update_treeview()  # Refresh the treeview
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Invalid input")


    # Add Instructor Form
    def add_instructor_form(self):
        tk.Label(self.instructor_tab, text="Instructor Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.instructor_tab, text="Age").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.instructor_tab, text="Email").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.instructor_tab, text="Instructor ID").grid(row=3, column=0, padx=10, pady=10)

        self.instructor_name_entry = tk.Entry(self.instructor_tab)
        self.instructor_age_entry = tk.Entry(self.instructor_tab)
        self.instructor_email_entry = tk.Entry(self.instructor_tab)
        self.instructor_id_entry = tk.Entry(self.instructor_tab)

        self.instructor_name_entry.grid(row=0, column=1)
        self.instructor_age_entry.grid(row=1, column=1)
        self.instructor_email_entry.grid(row=2, column=1)
        self.instructor_id_entry.grid(row=3, column=1)

        tk.Button(self.instructor_tab, text="Add Instructor", command=self.add_instructor).grid(row=4, column=1, pady=10)

    def add_instructor(self):
        name = self.instructor_name_entry.get()
        age = self.instructor_age_entry.get()
        email = self.instructor_email_entry.get()
        instructor_id = self.instructor_id_entry.get()

        if name and age.isdigit() and email and instructor_id:
            try:
                instructor = Instructor(name, int(age), email, instructor_id)
                instructors.append(instructor)
                messagebox.showinfo("Success", "Instructor added successfully")
                self.update_treeview()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Invalid input")

    # Add Course Form
    def add_course_form(self):
        tk.Label(self.course_tab, text="Course ID").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.course_tab, text="Course Name").grid(row=1, column=0, padx=10, pady=10)

        self.course_id_entry = tk.Entry(self.course_tab)
        self.course_name_entry = tk.Entry(self.course_tab)

        self.course_id_entry.grid(row=0, column=1)
        self.course_name_entry.grid(row=1, column=1)

        tk.Button(self.course_tab, text="Add Course", command=self.add_course).grid(row=2, column=1, pady=10)

    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()

        if course_id and course_name:
            course = Course(course_id, course_name)
            courses.append(course)
            messagebox.showinfo("Success", "Course added successfully")
            self.update_treeview()
        else:
            messagebox.showerror("Error", "Invalid input")
    
    def update_student_course_dropdown(self):
        # Print out the current lists
        print(f"Students list: {students}")
        print(f"Courses list: {courses}")
        
        # Populate student dropdown
        if students:
            student_names = [student.name for student in students]
            print(f"Populating student dropdown with: {student_names}")
            self.student_dropdown['values'] = student_names
        else:
            print("No students available to populate the dropdown.")
        
        # Populate course dropdown
        if courses:
            course_ids = [course.course_id for course in courses]
            print(f"Populating course dropdown with: {course_ids}")
            self.course_dropdown['values'] = course_ids
        else:
            print("No courses available to populate the dropdown.")




    # Register Student to Course
    def register_student_to_course(self):
        tk.Label(self.register_tab, text="Enter Student Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.register_tab, text="Enter Course ID").grid(row=1, column=0, padx=10, pady=10)

        self.selected_student = tk.StringVar()  # This will hold the selected student
        self.selected_course = tk.StringVar()  # This will hold the selected course

        # Initialize the student and course dropdowns
        self.student_dropdown = ttk.Combobox(self.register_tab, textvariable=self.selected_student)
        self.course_dropdown = ttk.Combobox(self.register_tab, textvariable=self.selected_course)

        # Set default width for the dropdowns (optional, for better visibility)
        self.student_dropdown.config(width=20)
        self.course_dropdown.config(width=20)

        # Place the dropdowns in the layout
        self.student_dropdown.grid(row=0, column=1)
        self.course_dropdown.grid(row=1, column=1)

        # Register button
        tk.Button(self.register_tab, text="Register", command=self.register_student).grid(row=2, column=1, pady=10)

        # Call to populate the dropdowns with data
        self.update_student_course_dropdown()


    def register_student(self):
        selected_student_name = self.selected_student.get()
        selected_course_id = self.selected_course.get()

        print(f"Selected student: {selected_student_name}, Selected course: {selected_course_id}")  # Debugging output

        student = next((s for s in students if s.name == selected_student_name), None)
        course = next((c for c in courses if c.course_id == selected_course_id), None)

        print(f"Student found: {student}, Course found: {course}")  # Debugging output

        if student and course:
            student.register_course(course)
            messagebox.showinfo("Success", f"{student.name} registered for {course.course_name}")
            self.update_treeview()  # Refresh treeview
        else:
            messagebox.showerror("Error", "Invalid selection")


    # Assign Instructor to Course
    def assign_instructor_to_course(self):
        tk.Label(self.assign_tab, text="Enter Instructor Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.assign_tab, text="Enter Course ID").grid(row=1, column=0, padx=10, pady=10)

        self.selected_instructor = tk.StringVar()
        self.selected_course_for_instructor = tk.StringVar()

        self.instructor_dropdown = ttk.Combobox(self.assign_tab, textvariable=self.selected_instructor)
        self.course_for_instructor_dropdown = ttk.Combobox(self.assign_tab, textvariable=self.selected_course_for_instructor)

        self.instructor_dropdown.grid(row=0, column=1)
        self.course_for_instructor_dropdown.grid(row=1, column=1)

        tk.Button(self.assign_tab, text="Assign", command=self.assign_instructor).grid(row=2, column=1, pady=10)
        self.update_instructor_course_dropdown()

    def assign_instructor(self):
        selected_instructor_name = self.selected_instructor.get()
        selected_course_id = self.selected_course_for_instructor.get()

        instructor = next((i for i in instructors if i.name == selected_instructor_name), None)
        course = next((c for c in courses if c.course_id == selected_course_id), None)

        if instructor and course:
            instructor.assign_course(course)
            messagebox.showinfo("Success", f"{instructor.name} assigned to {course.course_name}")
            self.update_treeview()
        else:
            messagebox.showerror("Error", "Invalid selection")

    # View Records in Treeview
    def view_records(self):
        columns = ("ID", "Name", "Type", "Details")

        self.tree = ttk.Treeview(self.view_tab, columns=columns, show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Details", text="Details")
        
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Add buttons for editing and deleting
        edit_button = tk.Button(self.view_tab, text="Edit Record", command=self.edit_record)
        edit_button.grid(row=1, column=0, sticky='ew', pady=10)

        delete_button = tk.Button(self.view_tab, text="Delete Record", command=self.delete_record)
        delete_button.grid(row=2, column=0, sticky='ew', pady=10)

        # Call update_treeview to populate records on startup
        self.update_treeview()

        # Make Treeview scrollable
        scrollbar = ttk.Scrollbar(self.view_tab, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.view_tab.grid_rowconfigure(0, weight=1)
        self.view_tab.grid_columnconfigure(0, weight=1)



    def update_treeview(self):
        # Clear the current records in the Treeview
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Add students
        for student in students:
            self.tree.insert("", "end", values=(student.student_id, student.name, "Student", f"Courses: {len(student.registered_courses)}"))

        # Add instructors
        for instructor in instructors:
            self.tree.insert("", "end", values=(instructor.instructor_id, instructor.name, "Instructor", f"Courses: {len(instructor.assigned_courses)}"))

        # Add courses
        for course in courses:
            instructor_name = course.instructor.name if course.instructor else "None"
            self.tree.insert("", "end", values=(course.course_id, course.course_name, "Course", f"Students: {len(course.enrolled_students)}, Instructor: {instructor_name}"))

    # Search Records
    def search_records(self):
        tk.Label(self.search_tab, text="Search by Name or ID").grid(row=0, column=0, padx=10, pady=10)

        self.search_entry = tk.Entry(self.search_tab)
        self.search_entry.grid(row=0, column=1)

        tk.Button(self.search_tab, text="Search", command=self.search).grid(row=0, column=2)

    def search(self):
        query = self.search_entry.get().lower()

        print(f"Search query: {query}")  # Debugging output

        # Clear the current Treeview records
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Search through students
        for student in students:
            print(f"Checking student: {student.name}, ID: {student.student_id}")  # Debugging output
            if query in student.name.lower() or query in str(student.student_id).lower():
                print(f"Match found: {student.name}")  # Debugging output
                self.tree.insert("", "end", values=(student.student_id, student.name, "Student", f"Courses: {len(student.registered_courses)}"))

        # Search through instructors
        for instructor in instructors:
            print(f"Checking instructor: {instructor.name}, ID: {instructor.instructor_id}")  # Debugging output
            if query in instructor.name.lower() or query in str(instructor.instructor_id).lower():
                print(f"Match found: {instructor.name}")  # Debugging output
                self.tree.insert("", "end", values=(instructor.instructor_id, instructor.name, "Instructor", f"Courses: {len(instructor.assigned_courses)}"))

        # Search through courses
        for course in courses:
            print(f"Checking course: {course.course_name}, ID: {course.course_id}")  # Debugging output
            if query in str(course.course_id).lower() or query in course.course_name.lower():
                print(f"Match found: {course.course_name}")  # Debugging output
                instructor_name = course.instructor.name if course.instructor else "None"
                self.tree.insert("", "end", values=(course.course_id, course.course_name, "Course", f"Students: {len(course.enrolled_students)}, Instructor: {instructor_name}"))

    def update_student_course_dropdown(self):
        self.student_dropdown['values'] = [student.name for student in students]
        self.course_dropdown['values'] = [course.course_id for course in courses]

    def update_instructor_course_dropdown(self):
        self.instructor_dropdown['values'] = [instructor.name for instructor in instructors]
        self.course_for_instructor_dropdown['values'] = [course.course_id for course in courses]

    def edit_record(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No record selected")
            return
        
        # Get record details from Treeview
        item = self.tree.item(selected_item)
        record_id, record_name, record_type, _ = item['values']

        # Determine the type (Student, Instructor, or Course)
        if record_type == "Student":
            student = next((s for s in students if str(s.student_id) == str(record_id)), None)
            if student:
                self.open_edit_window(student, "Student")
        elif record_type == "Instructor":
            instructor = next((i for i in instructors if str(i.instructor_id) == str(record_id)), None)
            if instructor:
                self.open_edit_window(instructor, "Instructor")
        elif record_type == "Course":
            course = next((c for c in courses if str(c.course_id) == str(record_id)), None)
            if course:
                self.open_edit_window(course, "Course")

    def open_edit_window(self, record, record_type):
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit {record_type}")

        if record_type == "Student":
            tk.Label(edit_window, text="Name").grid(row=0, column=0)
            tk.Label(edit_window, text="Age").grid(row=1, column=0)
            tk.Label(edit_window, text="Email").grid(row=2, column=0)

            name_entry = tk.Entry(edit_window)
            age_entry = tk.Entry(edit_window)
            email_entry = tk.Entry(edit_window)

            name_entry.insert(0, record.name)
            age_entry.insert(0, str(record.age))
            email_entry.insert(0, record._email)

            name_entry.grid(row=0, column=1)
            age_entry.grid(row=1, column=1)
            email_entry.grid(row=2, column=1)

            def save_changes():
                record.name = name_entry.get()
                record.age = int(age_entry.get())
                record._email = email_entry.get()
                self.update_treeview()  # Refresh treeview
                edit_window.destroy()

            tk.Button(edit_window, text="Save", command=save_changes).grid(row=3, column=1)
        # Similarly, handle Instructor and Course records

    def save_data(self):
        data = {
            "students": [{"id": s.student_id, "name": s.name, "age": s.age, "email": s._email, "courses": [c.course_id for c in s.registered_courses]} for s in students],
            "instructors": [{"id": i.instructor_id, "name": i.name, "age": i.age, "email": i._email, "courses": [c.course_id for c in i.assigned_courses]} for i in instructors],
            "courses": [{"id": c.course_id, "name": c.course_name, "instructor": c.instructor.instructor_id if c.instructor else None, "students": [s.student_id for s in c.enrolled_students]} for c in courses]
        }
        with open("school_data.json", "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Success", "Data saved successfully!")



    def delete_record(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No record selected")
            return
        
        # Get the selected record details
        item = self.tree.item(selected_item)
        record_id, record_name, record_type, _ = item['values']
        
        print(f"Selected Record for Deletion: {record_type}, ID: {record_id}, Name: {record_name}")  
        
        # Remove the record from the appropriate list
        if record_type == "Student":
            student = next((s for s in students if str(s.student_id) == str(record_id)), None)
            print(f"Student found: {student}")  
            if student:
                students.remove(student)
                print(f"Student {record_id} removed.")  
            else:
                print(f"Error: Student with ID {record_id} not found in list.")  # Error case
        elif record_type == "Instructor":
            instructor = next((i for i in instructors if str(i.instructor_id) == str(record_id)), None)
            print(f"Instructor found: {instructor}")  
            if instructor:
                instructors.remove(instructor)
                print(f"Instructor {record_id} removed.")  
            else:
                print(f"Error: Instructor with ID {record_id} not found in list.")  # Error case

        elif record_type == "Course":
            course = next((c for c in courses if str(c.course_id) == str(record_id)), None)
            print(f"Course found: {course}")  
            if course:
                courses.remove(course)
                print(f"Course {record_id} removed.")  
            else:
                print(f"Error: Course with ID {record_id} not found in list.")  # Error case


        # Save the updated data to the JSON file
        self.save_data()

        # Update the Treeview to reflect the changes
        self.update_treeview()

        messagebox.showinfo("Success", f"{record_type} record deleted")

    def load_data(self):
        try:
            with open("school_data.json", "r") as f:
                data = json.load(f)
            
            # Clear current records
            students.clear()
            instructors.clear()
            courses.clear()

            # Rebuild the data
            for student_data in data['students']:
                student = Student(student_data['name'], student_data['age'], student_data['email'], student_data['id'])
                students.append(student)

            for instructor_data in data['instructors']:
                instructor = Instructor(instructor_data['name'], instructor_data['age'], instructor_data['email'], instructor_data['id'])
                instructors.append(instructor)

            for course_data in data['courses']:
                course = Course(course_data['id'], course_data['name'])
                courses.append(course)

                # Re-link instructor and students
                if course_data['instructor']:
                    instructor = next((i for i in instructors if i.instructor_id == course_data['instructor']), None)
                    if instructor:
                        instructor.assign_course(course)
                
                for student_id in course_data['students']:
                    student = next((s for s in students if s.student_id == student_id), None)
                    if student:
                        student.register_course(course)

            self.update_treeview()  # Refresh the Treeview
            messagebox.showinfo("Success", "Data loaded successfully!")
        
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved data found!")
