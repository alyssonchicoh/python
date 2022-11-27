from src.layers.infra.datasources.contracts.ies.obter_todas_ies_data_source import ObterTodasIesDataSource
from src.layers.domain.entities.ies_entity import IesEntity


class ObterTodasIesDataSourcePostgresImpl(ObterTodasIesDataSource):
    def call(self) -> []:
        ies1 = IesEntity(1, "Teste2", "Teste", "Teste", "Teste", "Teste", "Teste", "Teste", "Teste", "Teste", "Teste")
        lista = [ies1, ies1, ies1]

        return lista
