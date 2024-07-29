class Course:
    def __init__(self, id: int, course_name: str):
        self.id = id
        self.course_name = course_name

    def __repr__(self):
        return f"Course(id={self.id}, course_name='{self.course_name}')"

