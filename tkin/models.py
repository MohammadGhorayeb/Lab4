"""
models.py

This module defines the core data models for the School Management System.

Classes:
    Person:
        Represents a generic person with attributes such as name, age, and email.
    Student(Person):
        Inherits from Person and represents a student with a student ID and registered courses.
    Instructor(Person):
        Inherits from Person and represents an instructor with an instructor ID and assigned courses.
    Course:
        Represents a course with attributes like course ID, name, instructor, and enrolled students.

Functions:
    is_valid_email(email: str) -> bool:
        Validates the format of an email address.
"""

import re

# Helper function to validate email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

class Person:
    def __init__(self, name: str, age: int, email: str):
        if not is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age
        self._email = email

class Student(Person):
    def __init__(self, name: str, age: int, email: str, student_id: str):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.registered_courses = []

    def register_course(self, course):
        self.registered_courses.append(course)
        course.add_student(self)

class Instructor(Person):
    def __init__(self, name: str, age: int, email: str, instructor_id: str):
        super().__init__(name, age, email)
        self.instructor_id = instructor_id
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.instructor = self

class Course:
    def __init__(self, course_id: str, course_name: str):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = None
        self.enrolled_students = []

    def add_student(self, student):
        self.enrolled_students.append(student)
