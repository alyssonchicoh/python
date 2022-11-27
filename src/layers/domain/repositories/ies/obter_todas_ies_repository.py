from abc import ABC, abstractmethod


class ObterTodasIesRepository(ABC):

    @abstractmethod
    def call(self) -> []:
        """ RETORNA UMA LISTA COM TODAS AS IES"""