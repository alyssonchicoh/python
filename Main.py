# -*- encoding:utf-8 -*-
from preenchimento_censo.PreenchimentoCensoIndicator import PreenchimentoCensoIndicator
from renovacao_automatica.RenovacaoAutomaticaService import RenovacaoAutomaticaService
from util.ImportData import ImportData

"""
    Main class. Responsible for running the application.
"""


class Main:

    @staticmethod
    def run():
        try:
            ImportData().generateCSV()
            #service = RenovacaoAutomaticaService()
            #service.run_course(2)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()
