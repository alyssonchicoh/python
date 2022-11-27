# -*- encoding:utf-8 -*-
from preenchimento_censo.PreenchimentoCensoIndicator import PreenchimentoCensoIndicator
from renovacao_automatica.RenovacaoAutomaticaService import RenovacaoAutomaticaService

"""
    Main class. Responsible for running the application.
"""


class Main:

    @staticmethod
    def run():
        try:
            service = RenovacaoAutomaticaService()
            service.run(1)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()
