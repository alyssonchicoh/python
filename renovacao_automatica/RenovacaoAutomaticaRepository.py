from renovacao_automatica.RenovacaoAutomatica import RenovacaoAutomatica
from util.GenericRepository import GenericRepository
from util.Scripts import Scripts


class RenovacaoAutomaticaRepository:

    def __init__(self):
        self._generic_repository = GenericRepository()

    def search(self):
        sql = Scripts().get_script(3, "")
        renovacao_list_db = self._generic_repository.search_by_sql(sql)
        return self._build_list(renovacao_list_db)

    def search_by_id_ies(self, id_ies):
        sql = Scripts().get_script(4, id_ies)
        renovacao_list_db = self._generic_repository.search_by_sql(sql)
        return self._build_list(renovacao_list_db)

    def search_by_id_course(self,id_course):
        sql = Scripts().get_script(7, id_course)
        renovacao_list_db = self._generic_repository.search_by_sql(sql)
        return self._build_list(renovacao_list_db)
    def _build_list(self, renovacao_list_db):
        renovacao_list = []

        for record in renovacao_list_db:
            renovacao_automatica = RenovacaoAutomatica()
            renovacao_automatica.to_renovacao_automatica(record)
            renovacao_automatica.print_renovacao()
            renovacao_list.append(renovacao_automatica)

        return renovacao_list
