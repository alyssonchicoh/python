from src.layers.domain.usecases.ies.obter_todas_ies_usecase import ObterTodasIesUseCaseImpl
from src.layers.infra.datasources.implementations.postgres.ies.ober_todos_ies_data_source_postgres_impl import \
    ObterTodasIesDataSourcePostgresImpl
from src.layers.infra.repositories.ies.obter_todas_ies_repository_impl import ObterTodasIesRepositoryImpl


def injetar_obter_todas_ies():
    datasource = ObterTodasIesDataSourcePostgresImpl()
    repository = ObterTodasIesRepositoryImpl(datasource)
    usecase = ObterTodasIesUseCaseImpl(repository)

    return usecase


