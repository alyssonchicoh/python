from util.GenericRepository import GenericRepository
from ies.IES import IES
from util.BDUtil import DBUtil


class IESRepository:

    def __init__(self):
        self._generic_repository = GenericRepository()

    def search(self):
        ies_list = []

        for item in self._generic_repository.search_all(DBUtil.TABLE_NAME_IES):
            ies = IES()
            ies.to_ies(item)
            ies_list.append(ies)

        return ies_list

    def save(self, ies):
        self._generic_repository.insert(DBUtil.TABLE_NAME_IES, ies.from_ies())
