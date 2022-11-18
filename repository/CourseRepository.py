from repository.GenericRepository import GenericRepository
from model.Course import Course
from utils.BDUtil import DBUtil


class CourseRepository:

    def __init__(self):
        self._generic_repository = GenericRepository()

    def search(self):
        configs = self._config_search()
        repository = self._generic_repository

        course_list_db = repository.search_all_with_inner_join(
            configs[0], configs[1], configs[2], configs[3],)

        course_list = []

        for item in course_list_db:
            course = Course()
            course.to_course(item)

            course_list.append(course)

        return course_list

    def _config_search(self):
        config = [
            DBUtil.TABLE_NAME_CURSO,
            DBUtil.TABLE_NAME_IES,
            DBUtil.COURSE_ID_IES_FK,
            DBUtil.IES_ID
        ]

        return config
