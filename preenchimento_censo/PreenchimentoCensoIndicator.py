from ies.IES import IES
from alarm.Alarm import Alarm
from preenchimento_censo.PreenchimentoCenso import PreenchimentoCenso
from ies.IESService import IESService
from preenchimento_censo.PreenchimentoCensoService import PreenchimentoCensoService
from alarm.AlarmService import AlarmService


class PreenchimentoCensoIndicator:

    def run(self, year):
        list_of_preenchimento_censo = self._search_preenchimento_censo(year)
        list_all_ies = self._search_ies()
        alarm_service = AlarmService()

        for ies in list_all_ies:
            alarm = self._check_ies_in_list_of_preenchimento_censo(
                ies, list_of_preenchimento_censo)

            if not alarm:
                alarm_service.save(self.build_alarm(ies,year))

    def _check_ies_in_list_of_preenchimento_censo(self, ies, list_of_preenchimento_censo):
        return any(ies.name == x.ies.name for x in list_of_preenchimento_censo)

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

    def build_alarm(self, ies, year):
        alarm = Alarm(ies_name=ies.name)
        alarm.correction_status = "NAO_CORRIGIDO"
        alarm.severity = "NORMAL"
        alarm.indicator_type = "CENSO_"+str(year)
        alarm.indicator_name = "PREENCHIMENTO DE CENSO"
        alarm.indicator_version = "1"
        alarm.ies_radical_cnpj = ies.radical_cnpj
        alarm.ies_cnpj = ies.cnpj
        alarm.ies_latitude = ies.latitude
        alarm.ies_longitude = ies.longitude
        alarm.ies_city = ies.city
        alarm.ies_state = ies.state
        alarm.ies_address = ies.address
        alarm.ies_sede = ies.head_office
        alarm.ies_sede_name = ies.head_office_name
        return alarm
