import sys
import os

# Add src/ to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from students.main import Student  # Import the Student class

def test_student():
    student = Student('Alice', '123', ['Math', 'Economics'])
    assert student.name == 'Alice'
    assert student.student_id == '123'
    assert student.courses == ['Math', 'Economics']

def test_enroll_course():
    student = Student('Alice', '123', ['Math', 'Economics'])
    student.enroll_course('Physics')
    assert student.courses == ['Math', 'Economics', 'Physics']

def test_get_courses():
    assert Student('Alice', '123', ['Math', 'Economics']).get_courses() == ['Math', 'Economics']
    assert Student('Alice', '123', []).get_courses() == []
    
