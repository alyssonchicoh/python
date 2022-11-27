from util.GenericRepository import GenericRepository
from util.BDUtil import DBUtil
from util.Scripts import Scripts
from alarm.Alarm import Alarm


class AlarmRepository:

    def __init__(self):
        self._generic_repository = GenericRepository()

    def save(self, alarm):
        sql = Scripts().get_script(2, alarm.from_alarm())
        self._generic_repository.insert_by_sql(sql)

    def search_nao_corrigido_by(self, ies_name, indicator_type):
        paramns = [ies_name, indicator_type]
        sql = Scripts().get_script(5, paramns)
        records = self._generic_repository.search_by_sql(sql)

        return self._build_list(records)

    def update_alarm(self, alarm_id, current_value, previous_value):
        paramns = [current_value, previous_value, alarm_id]
        sql = Scripts().get_script(6, paramns)
        self._generic_repository.insert_by_sql(sql)

    def _build_list(self, alarm_list_db):
        alarm_list = []

        for record in alarm_list_db:
            alarm = Alarm()
            alarm.to_alarm(record)
            alarm_list.append(alarm)

        return alarm_list
