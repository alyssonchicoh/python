from ies.IES import IES
from alarm.Alarm import Alarm
from preenchimento_censo.PreenchimentoCenso import PreenchimentoCenso
from ies.IESService import IESService
from preenchimento_censo.PreenchimentoCensoService import PreenchimentoCensoService
from alarm.AlarmService import AlarmService


class PreenchimentoCensoIndicator:

    def run(self):
        list_of_preenchimento_censo = self._search_preenchimento_censo(2022)
        list_all_ies = self._search_ies()
        alarm_service = AlarmService()

        for ies in list_all_ies:
            alarm = any(
                ies.name == x.ies.name for x in list_of_preenchimento_censo)
            if (alarm):
                alarm_service.save(self.build_alarm(ies))

    def _search_ies(self):
        service = IESService()
        ies = service.search()
        return ies

    def _search_preenchimento_censo(self, year):
        service = PreenchimentoCensoService()
        return service.search(year)

    def _construirIES(self, name, number):
        return IES(name=name)

    def _construirPreenchimentoCenso(self, ies):
        return PreenchimentoCenso(ies=ies)

    def build_alarm(self, ies):
        alarm = Alarm(ies_name=ies.name)
        return alarm
