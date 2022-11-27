from renovacao_automatica.RenovacaoAutomatica import RenovacaoAutomatica
from renovacao_automatica.RenovacaoAutomaticaRepository import RenovacaoAutomaticaRepository
from ies.IESService import IESService
from alarm.AlarmService import AlarmService
from alarm.Alarm import Alarm


class RenovacaoAutomaticaService:

    def __init__(self):
        self._repository = RenovacaoAutomaticaRepository()
        self._ies_service = IESService()
        self._alarm_service = AlarmService()

    def search(self):
        return self._repository.search()

    def search_by_id_ies(self, id_ies):
        return self._repository.search_by_id_ies(id_ies)

    def run(self, limiar):
        ies_list = self._ies_service.search()

        for ies in ies_list:
            renovacoes_ies = self.search_by_id_ies(ies.id)

            if len(renovacoes_ies) >= limiar:
                self._alarm_service.save(self.build_alarm(ies))

    def build_alarm(self, ies):
        alarm = Alarm(ies_name=ies.name)
        alarm.correction_status = "NAO_CORRIGIDO"
        alarm.severity = "NORMAL"
        alarm.indicator_type = "2_RENOVACOES_AUTOMATICA"
        alarm.indicator_name = "RENOVAÇÃO AUTOMÁTICA"
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
