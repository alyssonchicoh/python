from preenchimento_censo.PreenchimentoCensoRepository import PreenchimentoCensoRepository


class PreenchimentoCensoService:

    def __init__(self):
        self._repository = PreenchimentoCensoRepository()

    def search(self, year):
        return self._repository.search_by_year(year)
