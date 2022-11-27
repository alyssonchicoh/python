from util.GenericRepository import GenericRepository
from preenchimento_censo.PreenchimentoCenso import PreenchimentoCenso
from util.BDUtil import DBUtil
from util.Scripts import Scripts


class PreenchimentoCensoRepository:

    def __init__(self):
        self._generic_repository = GenericRepository()

    def search_by_year(self, year):
        sql = Scripts().get_script(1, year)

        preenchimento_list_db = self._generic_repository.search_by_sql(sql)
        preenchimento_list = []

        for record in preenchimento_list_db:
            preenchimento = PreenchimentoCenso()
            preenchimento.to_preenchimento_censo(record)
            preenchimento_list.append(preenchimento)

        return preenchimento_list
