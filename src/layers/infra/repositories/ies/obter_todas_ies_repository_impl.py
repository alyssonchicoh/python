from src.layers.domain.repositories.ies.obter_todas_ies_repository import ObterTodasIesRepository
from src.layers.infra.datasources.contracts.ies.obter_todas_ies_data_source import ObterTodasIesDataSource


class ObterTodasIesRepositoryImpl(ObterTodasIesRepository):

    def __init__(self, obter_todas_ies_data_source: ObterTodasIesDataSource):
        self.__obter_todas_ies_data_source = obter_todas_ies_data_source

    def call(self) -> []:
        return self.__obter_todas_ies_data_source.call()
