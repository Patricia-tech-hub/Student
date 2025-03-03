import sys
import os

# Add src/ to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from students.main import Student

student_1 = Student('Kim', '201', ['English', 'Math', 'Science'])
print(student_1.name)
print(student_1.student_id)
print(student_1.courses)
student_1.enroll_course('History')
print(student_1.courses)
student_1.get_courses()