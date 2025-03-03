class Student:
    def __init__(self, name, student_id, courses):
        ''' (Student, str, str, list of str) -> NoneType
        Create a new student with name, student_id, and courses.
        '''
        assert type(name) == str
        assert type(student_id) == str
        assert type(courses) == list
        for course in courses:
            assert type(course) == str
        self.name = name
        self.student_id = student_id
        self.courses = courses
    def enroll_course(self, course):
        ''' (Student, str) -> NoneType	
        Enroll the student in the course.
        '''
        assert type(course) == str
        self.courses.append(course)
    def get_courses(self):
        ''' (Student) -> list of str
        Return the courses the student is enrolled in.
        '''
        return self.courses
    

    

    