from typing import List, Optional
from address import Address
from models.course import Course

class User:
    def __init__(self, id: int, name: str, age: int, email: str, address: Optional[Address] = None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.courses: List[Course] = []

    def add_course(self, course: 'Course'):
        self.courses.append(course)

    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', age={self.age}, "
                f"email='{self.email}', address={self.address}, courses={self.courses})")
