from util.BDUtil import DBUtil


class Alarm:

    def __init__(self, id="", date="", correction_date="", correction_status="",
                 severity="", indicator_type="", indicator_name="", indicator_version="",
                 ies_name="", ies_radical_cnpj="", ies_cnpj="", ies_latitude="", ies_longitude="",
                 ies_city="", ies_state="", ies_address="", ies_group="", ies_sede="", ies_sede_name="", course_name="", course_area="",
                 course_workload="",
                 ):

        self._id = id
        self._date = date
        self._correction_date = correction_date
        self._correction_status = correction_status
        self._severity = severity
        self._indicator_type = indicator_type
        self._indicator_name = indicator_name
        self._indicator_version = indicator_version
        self._ies_name = ies_name
        self._ies_radical_cnpj = ies_radical_cnpj
        self._ies_cnpj = ies_cnpj
        self._ies_latitude = ies_latitude
        self._ies_longitude = ies_longitude
        self._ies_city = ies_city
        self._ies_state = ies_state
        self._ies_address = ies_address
        self._ies_group = ies_group
        self._ies_sede = ies_sede
        self._ies_sede_name = ies_sede_name
        self._course_name = course_name
        self._course_area = course_area
        self._course_workload = course_workload

    def from_alarm(self):
        values = {
            DBUtil.ALARM_ID: self._id,
            DBUtil.ALARM_CORRECTION_STATUS: self._correction_status,
            DBUtil.ALARM_INDICATOR_TYPE: self._indicator_type,
            DBUtil.ALARM_INDICATOR_NAME: self._indicator_name,
            DBUtil.ALARM_INDICATOR_VERSION: self.indicator_version,
            DBUtil.ALARM_IES_NAME: "'"+self._ies_name+"'",
            DBUtil.ALARM_IES_RADICAL_CNPJ: self._ies_radical_cnpj,
            DBUtil.ALARM_IES_CNPJ: self._ies_cnpj,
            DBUtil.ALARM_IES_LATITUDE: self._ies_latitude,
            DBUtil.ALARM_IES_LONGITUDE: self._ies_longitude,
            DBUtil.ALARM_IES_CITY: self._ies_city,
            DBUtil.ALARM_IES_STATE: self._ies_state,
            DBUtil.ALARM_IES_ADDRESS: self._ies_address,
            DBUtil.ALARM_IES_GROUP: self._ies_group,
            DBUtil.ALARM_IES_SEDE: self._ies_sede,
            DBUtil.ALARM_IES_SEDE_NAME: self._ies_sede_name,
            DBUtil.ALARM_COURSE_NAME: self._course_name,
            DBUtil.ALARM_COURSE_AREA: self._course_area,
            DBUtil.ALARM_COURSE_WORKLOAD: self._course_workload
        }

        return values

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def correction_date(self):
        return self._correction_date

    @property
    def correction_status(self):
        return self._correction_status

    @property
    def severity(self):
        return self._severity

    @property
    def indicator_type(self):
        return self._indicator_type

    @property
    def indicator_name(self):
        return self._indicator_name

    @property
    def indicator_version(self):
        return self._indicator_version

    @property
    def ies_name(self):
        return self._ies_name

    @property
    def ies_radical_cnpj(self):
        return self._ies_radical_cnpj

    @property
    def ies_cnpj(self):
        return self._ies_cnpj

    @property
    def ies_latitude(self):
        return self._ies_latitude

    @property
    def ies_longitude(self):
        return self._ies_longitude

    @property
    def ies_city(self):
        return self._ies_city

    @property
    def ies_state(self):
        return self._ies_state

    @property
    def ies_address(self):
        return self._ies_address

    @property
    def ies_group(self):
        return self._ies_group

    @property
    def ies_sede(self):
        return self._ies_sede

    @property
    def course_name(self):
        return self._course_name

    @property
    def course_area(self):
        return self._course_area

    @property
    def workload(self):
        return self._wordload
