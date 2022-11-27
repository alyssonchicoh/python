from util.GenericRepository import GenericRepository
from util.BDUtil import DBUtil
from util.Scripts import Scripts


class AlarmRepository:

    def __init__(self):
        self._generic_repository = GenericRepository()

    def save(self, alarm):
        sql = Scripts().get_script(2, alarm.from_alarm())
        print(sql)
        self._generic_repository.insert_by_sql(sql)
