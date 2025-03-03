# Student Management System

This is a simple Python project that defines a `Student` class with methods to manage student enrollments.

## Features

- Store student **name**, **student ID**, and **enrolled courses**.
- Enroll students in courses using the `enroll_course(course)` method.
- Retrieve enrolled courses using the `get_courses()` method.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project-directory>
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Import the `Student` class in your Python script:
    ```python
    from students.main import Student
    ```

2. Create a new student:
    ```python
    student = Student('Alice', '123', ['Math', 'Economics'])
    ```

3. Enroll the student in a new course:
    ```python
    student.enroll_course('Physics')
    ```

4. Retrieve the list of enrolled courses:
    ```python
    courses = student.get_courses()
    print(courses)  # Output: ['Math', 'Economics', 'Physics']
    ```

## Running Tests

To run the tests, use the following command:
```sh
pytest