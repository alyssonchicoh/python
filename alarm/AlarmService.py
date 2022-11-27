from alarm.Alarm import Alarm
from alarm.AlarmRepository import AlarmRepository


class AlarmService:

    def __init__(self):
        self._repository = AlarmRepository()

    def save(self, alarm):
        self._repository.save(alarm)

    def search_nao_corrigido_by_ies_and_indicator_type(self, ies_name, indicator_type):
        return self._repository.search_nao_corrigido_by(ies_name, indicator_type)

    def update_alarm(self, alarm_id, current_value, previous_value):
        return self._repository.update_alarm(alarm_id, current_value, previous_value)
