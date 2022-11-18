# -*- encoding:utf-8 -*-
from service.IESService import IESService
from service.CourseService import CourseService

from repository.GenericRepository import GenericRepository
from model.IES import IES
from indicator.PreenchimentoCensoIndicator import PreenchimentoCensoIndicator


"""
    Main class. Responsible for running the application.
"""


class Main:

    @staticmethod
    def run():
        try:

            # dados = {
            #    'name': 'nome do registro',
            #    'cidade': 'Fortaleza',
            #    'estado': 'Ceara'
            # }

            id = 1
            name = "UFC"
            cnpj = "11111"
            radical_cnpj = "11"
            city = "Fortaleza"
            state = "CE"
            address = "teste"
            latitude = "111"
            longitude = "222"
            head_office = "false"
            head_office_name = ""

            ies = IES(
                id, name, cnpj, radical_cnpj,
                city, state, address, latitude,
                longitude, head_office, head_office_name)

        #    service = CourseService()

          #  for item in service.search():
           #     item.print()
            #    print("----")

            run = PreenchimentoCensoIndicator()
            run.run()

        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()
