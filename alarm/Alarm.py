from util.BDUtil import DBUtil


class Alarm:

    def __init__(self, id="", date="", correction_date="", correction_status="",
                 severity="", indicator_type="", indicator_name="", indicator_version="",
                 current_value="", previous_value="", ies_name="", ies_radical_cnpj="",
                 ies_cnpj="", ies_latitude="", ies_longitude="", ies_city="", ies_state="",
                 ies_address="", ies_group="", ies_sede="", ies_sede_name="", course_name="",
                 course_area="", course_workload="",
                 ):

        self._id = id
        self._date = date
        self._correction_date = correction_date
        self._correction_status = correction_status
        self._severity = severity
        self._indicator_type = indicator_type
        self._indicator_name = indicator_name
        self._indicator_version = indicator_version
        self._current_value = current_value
        self._previous_value = previous_value
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
        print("teste")
        values = {
            DBUtil.ALARM_CORRECTION_STATUS: self._to_string_db(self._correction_status),
            DBUtil.ALARM_SEVERITY:  self._to_string_db(self._severity),
            DBUtil.ALARM_INDICATOR_TYPE: self._to_string_db(self._indicator_type),
            DBUtil.ALARM_INDICATOR_NAME: self._to_string_db(self._indicator_name),
            DBUtil.ALARM_INDICATOR_VERSION: self._to_string_db(self._indicator_version),
            DBUtil.ALARM_CURRENT_VALUE: self._to_string_db(self._current_value),
            DBUtil.ALARM_PREVIOUS_VALUE: '',
            DBUtil.ALARM_IES_NAME: self._to_string_db(self._ies_name),
            DBUtil.ALARM_IES_RADICAL_CNPJ: self._to_string_db(self._ies_radical_cnpj),
            DBUtil.ALARM_IES_CNPJ: self._to_string_db(self._ies_cnpj),
            DBUtil.ALARM_IES_LATITUDE: self._to_string_db(self._ies_latitude),
            DBUtil.ALARM_IES_LONGITUDE: self._to_string_db(self._ies_longitude),
            DBUtil.ALARM_IES_CITY: self._to_string_db(self._ies_city),
            DBUtil.ALARM_IES_STATE: self._to_string_db(self._ies_state),
            DBUtil.ALARM_IES_ADDRESS: self._to_string_db(self._ies_address),
            DBUtil.ALARM_IES_GROUP: self._to_string_db(self._ies_group),
            DBUtil.ALARM_IES_SEDE: 'true',
            DBUtil.ALARM_IES_SEDE_NAME: self._to_string_db(self._ies_sede_name),
            DBUtil.ALARM_COURSE_NAME: self._to_string_db(self._course_name),
            DBUtil.ALARM_COURSE_AREA: self._to_string_db(self._course_area),
            DBUtil.ALARM_COURSE_WORKLOAD: self._to_string_db(
                self._course_workload)
        }

        return values

    def to_alarm(self, record):
        self._id = record[0]
        self._current_value = record[8]

    def _to_string_db(self, value):
        if isinstance(value, type(None)):
            return ''
        else:
            return "'"+value+"'"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def correction_date(self):
        return self._correction_date

    @correction_date.setter
    def correction_date(self, correction_date):
        self._correction_date = correction_date

    @property
    def correction_status(self):
        return self._correction_status

    @correction_status.setter
    def correction_status(self, correction_status):
        self._correction_status = correction_status

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, severity):
        self._severity = severity

    @property
    def indicator_type(self):
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        self._indicator_type = indicator_type

    @property
    def indicator_name(self):
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        self._indicator_name = indicator_name

    @property
    def indicator_version(self):
        return self._indicator_version

    @indicator_version.setter
    def indicator_version(self, indicator_version):
        self._indicator_version = indicator_version

    @property
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        self._current_value = current_value

    @property
    def previous_value(self):
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value):
        self._previous_value = previous_value

    @property
    def ies_name(self):
        return self._ies_name

    @ies_name.setter
    def ies_name(self, ies_name):
        self._ies_name = ies_name

    @property
    def ies_radical_cnpj(self):
        return self._ies_radical_cnpj

    @ies_radical_cnpj.setter
    def ies_radical_cnpj(self, ies_radical_cnpj):
        self._ies_radical_cnpj = ies_radical_cnpj

    @property
    def ies_cnpj(self):
        return self._ies_cnpj

    @ies_cnpj.setter
    def ies_cnpj(self, ies_cnpj):
        self._ies_cnpj = ies_cnpj

    @property
    def ies_latitude(self):
        return self._ies_latitude

    @ies_latitude.setter
    def ies_latitude(self, ies_latitude):
        self._ies_latitude = ies_latitude

    @property
    def ies_longitude(self):
        return self._ies_longitude

    @ies_longitude.setter
    def ies_longitude(self, ies_longitude):
        self._ies_longitude = ies_longitude

    @property
    def ies_city(self):
        return self._ies_city

    @ies_city.setter
    def ies_city(self, ies_city):
        self._ies_city = ies_city

    @property
    def ies_state(self):
        return self._ies_state

    @ies_state.setter
    def ies_state(self, ies_state):
        self._ies_state = ies_state

    @property
    def ies_address(self):
        return self._ies_address

    @ies_address.setter
    def ies_address(self, ies_address):
        self._ies_address = ies_address

    @property
    def ies_group(self):
        return self._ies_group

    @ies_group.setter
    def ies_group(self, ies_group):
        self._ies_group = ies_group

    @property
    def ies_sede(self):
        return self._ies_sede

    @ies_sede.setter
    def ies_sede(self, ies_sede):
        self._ies_sede = ies_sede

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, course_name):
        self._course_name = course_name

    @property
    def course_area(self):
        return self._course_area

    @course_area.setter
    def course_area(self, course_area):
        self._course_area = course_area

    @property
    def workload(self):
        return self._wordload

    @workload.setter
    def workload(self, workload):
        self._workload = workload
