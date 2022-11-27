from util.BDUtil import DBUtil


class IES:

    def __init__(
            self, id="", name="", cnpj="", radical_cnpj="",
            city="", state="", address="", latitude="",
            longitude="", head_office="", head_office_name=""):

        self._id = id
        self._name = name
        self._cnpj = cnpj
        self._radical_cnpj = radical_cnpj
        self._city = city
        self._state = state
        self._address = address
        self._latitude = latitude
        self._longitude = longitude
        self._head_office = head_office
        self._head_office_name = head_office_name

    def from_ies(self):
        values = {
            DBUtil.IES_ID: self._id,
            DBUtil.IES_NAME: self._name,
            DBUtil.IES_CNPJ: self._cnpj,
            DBUtil.IES_RADICAL_CNPJ: self._radical_cnpj,
            DBUtil.IES_CITY: self._city,
            DBUtil.IES_STATE: self._state,
            DBUtil.IES_ADDRESS: self._address,
            DBUtil.IES_LATITUDE: self._latitude,
            DBUtil.IES_LONGITUDE: self._longitude,
            DBUtil.IES_HEAD_OFFICE: self._head_office,
            DBUtil.IES_HEAD_OFFICE_NAME: self._head_office_name,
        }

        return values

    def to_ies(self, record, shift=0):
        self._id = record[shift + 0]
        self._name = record[shift + 1]
        self._cnpj = record[shift + 2]
        self._radical_cnpj = record[shift + 3]
        self._city = record[shift + 4]
        self._state = record[shift + 5]
        self._address = record[shift + 6]
        self._latitude = record[shift + 7]
        self._longitude = record[shift + 8]
        self._head_office = record[shift + 9]
        self._head_office_name = record[shift + 0]

    def print_ies(self):
        print("ID: " + str(self._id))
        print("NOME: " + str(self._name))
        print("CNPJ: " + str(self._cnpj))
        print("RADICAL_CNPJ: " + str(self._radical_cnpj))
        print("CIDADE: " + str(self._city))
        print("ESTADO: " + str(self._state))
        print("ENDEREÇO: " + str(self._address))
        print("LATITUDE: " + str(self._latitude))
        print("LONGITUDE: " + str(self._longitude))
        print("IES_SEDE: " + str(self._head_office))
        print("NOME_SEDE: " + str(self._head_office_name))

    @ property
    def id(self):
        return self._id

    @ property
    def name(self):
        return self._name

    @ property
    def cnpj(self):
        return self._cnpj

    @ property
    def radical_cnpj(self):
        return self.radical_cnpj

    @ property
    def city(self):
        return self._city

    @ property
    def state(self):
        return self._state

    @ property
    def address(self):
        return self._address

    @ property
    def latitude(self):
        return self._latitude

    @ property
    def longitude(self):
        return self._longitude

    @ property
    def head_office(self):
        return self._head_office

    @ property
    def head_office_name(self):
        return self._head_office_name
