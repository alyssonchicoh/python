from alarm.Alarm import Alarm
from alarm.AlarmRepository import AlarmRepository


class AlarmService:

    def __init__(self):
        self._repository = AlarmRepository()

    def save(self, alarm):
        self._repository.save(alarm)
