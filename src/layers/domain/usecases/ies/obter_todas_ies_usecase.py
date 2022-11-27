from abc import ABC, abstractmethod

from src.layers.domain.repositories.ies.obter_todas_ies_repository import ObterTodasIesRepository


class ObterTodasIesUseCase(ABC):

    @abstractmethod
    def call(self) -> []:
        """ RETORNA UMA LISTA COM TODAS AS IES"""


class ObterTodasIesUseCaseImpl(ObterTodasIesUseCase):

    def __init__(self, obter_todas_ies_repository: ObterTodasIesRepository):
        self.__obter_todas_ies_repository = obter_todas_ies_repository

    def call(self) -> []:
        return self.__obter_todas_ies_repository.call()
