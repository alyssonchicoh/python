from course.CourseRepository import CourseRepository


class CourseService:

    def __init__(self):
        self._course_repository = CourseRepository()

    def search(self):
        return self._course_repository.search()
