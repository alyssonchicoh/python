# -*- encoding:utf-8 -*-
from alarm.Alarm import Alarm
from alarm.AlarmService import AlarmService
from ies.IES import IES
from ies.IESService import IESService


"""
    Main class. Responsible for running the application.
"""


class Main:

    @staticmethod
    def run():
        try:
            alarm = Alarm()
            service = IESService()
            lista = service.search()

            for l in lista:
                l.print_ies()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()
