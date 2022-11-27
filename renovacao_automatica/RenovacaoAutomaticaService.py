from renovacao_automatica.RenovacaoAutomaticaRepository import RenovacaoAutomaticaRepository
from ies.IESService import IESService
from alarm.AlarmService import AlarmService
from course.CourseService import CourseService
from alarm.Alarm import Alarm


class RenovacaoAutomaticaService:

    def __init__(self):
        self._repository = RenovacaoAutomaticaRepository()
        self._ies_service = IESService()
        self._alarm_service = AlarmService()
        self._course_service = CourseService()

    def search(self):
        return self._repository.search()

    def search_by_id_ies(self, id_ies):
        return self._repository.search_by_id_ies(id_ies)

    def search_by_id_course(self, id_course):
        return self._repository.search_by_id_course(id_course)
    def run(self, limiar):
        ies_list = self._ies_service.search()

        for ies in ies_list:
            renovacoes_ies = self.search_by_id_ies(ies.id)
            qtd_renovacoes = len(renovacoes_ies)

            if qtd_renovacoes >= limiar:
                self._save_alarm(ies, qtd_renovacoes, qtd_renovacoes)

    def run_course(self, limiar):
        course_list = self._course_service.search()

        for course in course_list:
            renovacoes_ies = self.search_by_id_course(course.id)
            qtd_renovacoes = len(renovacoes_ies)

            if qtd_renovacoes >= limiar:
                self._save_alarm_with_course(course.ies, course, qtd_renovacoes, qtd_renovacoes)

    def _save_alarm(self, ies, old_qtd, new_qtd):
        alarms = self._check_exits_alarm(ies.name)

        if len(alarms) == 0:
            alarm = self.build_alarm(ies, old_qtd, new_qtd)
            self._alarm_service.save(alarm)
        else:
            self._alarm_service.update_alarm(
                alarms[0].id, new_qtd, alarms[0].current_value)
    def _save_alarm_with_course(self, ies,couse, old_qtd, new_qtd):
        alarms = self._check_exits_alarm(ies.name)

        if len(alarms) == 0:
            alarm = self.build_alarm_with_course(ies, couse, old_qtd, new_qtd)
            self._alarm_service.save(alarm)
        else:
            self._alarm_service.update_alarm(alarms[0].id, new_qtd, alarms[0].current_value)

    def _check_exits_alarm(self, ies_name):
        return self._alarm_service.search_nao_corrigido_by_ies_and_indicator_type(ies_name, "2_RENOVACOES_AUTOMATICA")

    def build_alarm(self, ies, old_qtd_records, new_qtd_records):
        alarm = Alarm(ies_name=ies.name)
        alarm.correction_status = "NAO_CORRIGIDO"
        alarm.severity = "NORMAL"
        alarm.indicator_type = "2_RENOVACOES_AUTOMATICA"
        alarm.indicator_name = "RENOVAÇÃO AUTOMÁTICA"
        alarm.indicator_version = "1"
        alarm.current_value = str(new_qtd_records)
        alarm.previous_value = str(old_qtd_records)
        alarm.ies_radical_cnpj = ies.radical_cnpj
        alarm.ies_cnpj = ies.cnpj
        alarm.ies_latitude = ies.latitude
        alarm.ies_longitude = ies.longitude
        alarm.ies_city = ies.city
        alarm.ies_state = ies.state
        alarm.ies_address = ies.address
        alarm.ies_sede = ies.head_office
        alarm.ies_sede_name = ies.head_office_name

    def build_alarm_with_course(self, ies, course, old_qtd_records, new_qtd_records):
        alarm = Alarm(ies_name=ies.name)
        alarm.correction_status = "NAO_CORRIGIDO"
        alarm.severity = "NORMAL"
        alarm.indicator_type = "2_RENOVACOES_AUTOMATICA_CURSOR"
        alarm.indicator_name = "RENOVAÇÃO AUTOMÁTICA DE CURSO"
        alarm.indicator_version = "1"
        alarm.current_value = str(new_qtd_records)
        alarm.previous_value = str(old_qtd_records)
        alarm.ies_radical_cnpj = ies.radical_cnpj
        alarm.ies_cnpj = ies.cnpj
        alarm.ies_latitude = ies.latitude
        alarm.ies_longitude = ies.longitude
        alarm.ies_city = ies.city
        alarm.ies_state = ies.state
        alarm.ies_address = ies.address
        alarm.ies_sede = ies.head_office
        alarm.ies_sede_name = ies.head_office_name
        alarm.course_name = course.name
        alarm.course_area = course.area
        return alarm
