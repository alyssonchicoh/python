from renovacao_automatica.RenovacaoAutomatica import RenovacaoAutomatica
from util.GenericRepository import GenericRepository
from util.BDUtil import DBUtil
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

    def _build_list(self, renovacao_list_db):
        renovacao_list = []

        for record in renovacao_list_db:
            renovacaoAutomatica = RenovacaoAutomatica()
            renovacaoAutomatica.to_renovacao_automatica(record)
            renovacaoAutomatica.print_renovacao()
            renovacao_list.append(renovacaoAutomatica)

        return renovacao_list
