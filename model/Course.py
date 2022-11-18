from utils.BDUtil import DBUtil
from model.IES import IES


class Course:

    def __init__(self, id="", name="", area="", workload="", ies=IES):
        self._id = id
        self._name = name
        self._area = area
        self._worload = workload
        self._ies = ies

    def print(self):
        print("ID:" + str(self._id))
        print("NAME:" + self._name)
        print("AREA:" + self._area)
        print("WORLOAD:" + str(self._worload))
        print("IES:")
        print(self._ies.print_ies())

    # CONVERTE UM OBJETO DE CURSO EM UM DICT PARA INSERIR NO BD

    def from_course(self):
        values = {
            DBUtil.COURSE_ID: self._id,
            DBUtil.COURSE_NAME: self._name,
            DBUtil.COURSE_AREA: self._area,
            DBUtil.COURSE_WORKLOAD: self._worload,
            DBUtil.COURSE_ID_IES_FK: self._ies.id,
        }
        return values

    # TRANSFORMA UMA TUPLA VINDA DO BD EM OBJETO
    def to_course(self, record):
        self._id = record[0]
        self._name = record[1]
        self._are = record[2]
        self._worload = record[3]
        self._ies = self._build_ies(record, 5)

    # CONSTROI UM OBJETO IES
    # RECEBE A TUPLA E Q QUANTIDADE DE DADOS REFERENTE AO CURSO NO SELECT
    def _build_ies(self, record, quantity_of_elements_course):
        ies = IES()
        ies.to_ies(record, quantity_of_elements_course)

        return ies

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def area(self):
        return self._area

    @property
    def workload(self):
        return self._workload

    @property
    def ies(self):
        return self._ies
