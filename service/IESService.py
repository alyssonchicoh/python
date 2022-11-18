from model.IES import IES
from repository.IESRepository import IESRepository


class IESService():

    def __init__(self):
        self._ies_repository = IESRepository()

    def search(self):
        return self._ies_repository.search()

    def save(self, ies):
        self._ies_repository.save(ies)
