from abc import ABC, abstractmethod


class ObterTodasIesDataSource(ABC):

    @abstractmethod
    def call(self) -> []:
        """ RETORNA UMA LISTA COM TODAS AS IES"""