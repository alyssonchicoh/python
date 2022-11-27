class IesEntity:
    def __init__(self, pk, nome, cnpj, radical_cnpj, cidade, estado, endereco, latitude, longitude, is_sede, nome_sede):
        self.__pk = pk
        self.__nome = nome
        self.__cnpj = cnpj
        self.__radical_cnpj = radical_cnpj
        self.__cidade = cidade
        self.__estado = estado
        self.__endereco = endereco
        self.__latitude = latitude
        self.__longitude = longitude
        self.__is_sede = is_sede
        self.__nome_sede = nome_sede

    def print(self):
        print(str(self.__pk) + " - " +self.__nome)
