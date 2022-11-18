from model.IES import IES
from model.Course import Course
from utils.BDUtil import DBUtil


class PreenchimentoCenso:

    def __init__(self, id="", date="", ies=IES, course=Course):
        self._id = id
        self._date = date
        self._ies = ies
        self._course = course

    def from_preenchimento_censo(self):
        values = {
            DBUtil.PREENCHIMENTO_CENSO_ID: self._id,
            DBUtil.PREENCHIMENTO_CENSO_DATE: self._date,
            DBUtil.PREENCHIMENTO_CENSO_IES: self._ies.id,
            DBUtil.PREENCHIMENTO_CENSO_COURSE: self._course.id,
        }

        return values

    # TRANSFORMA UMA TUPLA VINDA DO BD EM OBJETO
    def to_course(self, record):
        self._id = record[0]
        self._date = record[1]
        self._ies = self.__build_ies(record, 3)

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
    def date(self):
        return self._date

    @property
    def ies(self):
        return self._ies

    @property
    def course(self):
        return self._couse
