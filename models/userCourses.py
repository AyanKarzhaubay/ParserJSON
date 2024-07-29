class UserCourse:
    def __init__(self, user_id: int, course_id: int):
        self.user_id = user_id
        self.course_id = course_id

    def __repr__(self):
        return f"UserCourse(user_id={self.user_id}, course_id={self.course_id})"

