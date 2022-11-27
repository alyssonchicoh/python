from util.BDUtil import DBUtil
from ies.IES import IES


class RenovacaoAutomatica:

    def __init__(self, id="", renovacao_date="", vencimento_date="", type_sequential="", ies=""):
        self._id = id
        self._renovacao_date = renovacao_date
        self._vencimento_date = vencimento_date
        self._type_sequential = type_sequential
        self._ies = ies

    def print_renovacao(self):
        print("ID" + str(self._id))
        print("DATA" + str(self._renovacao_date))
        print("VENCIMENTO" + str(self._vencimento_date))
        print("SEQUENTIAL" + str(self._type_sequential))
        print(str(self._ies.print_ies()))

    def from_renovacao_automatica(self):
        values = {
            DBUtil.RENOVACAO_AUTOMATICA_ID: self._id,
            DBUtil.RENOVACAO_AUTOMATICA_DATE_RENOVACAO: self._renovacao_date,
            DBUtil.RENOVACAO_AUTOMATICA_DATE_VENCIMENTO: self._vencimento_date,
            DBUtil.RENOVACAO_AUTOMATICA_SEQUENTIAL_TYPE: self._type_sequential,
            DBUtil.RENOVACAO_AUTOMATICA_IES: self._ies.id,
        }

        return values

    def to_renovacao_automatica(self, record):
        self._id = record[0]
        self._renovacao_date = record[1]
        self._vencimento_date = record[2]
        self._type_sequential = record[3]
        self._ies = self._build_ies(record, 7)

    def _build_ies(self, record, quantity_of_elements_course):
        ies = IES()
        ies.to_ies(record, quantity_of_elements_course)

        return ies

    @property
    def id(self):
        return self._id

    @property
    def renovacao_date(self):
        return self._renovacao_date

    @property
    def vencimento_date(self):
        return self._vencimento_date

    @property
    def type_sequential(self):
        return self._type_sequential

    @property
    def ies(self):
        return self._ies
