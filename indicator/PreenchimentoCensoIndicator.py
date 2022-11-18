from model.IES import IES
from model.PreenchimentoCenso import PreenchimentoCenso


class PreenchimentoCensoIndicator:

    def run(self):
        list_of_preenchimento_censo = []
        list_all_ies = []

        ies1 = self._construirIES("UNIFOR", 1)
        ies2 = self._construirIES("UFC", 2)
        ies3 = self._construirIES("UECE", 3)
        ies4 = self._construirIES("FA7", 4)
        ies5 = self._construirIES("FFB", 5)

        list_all_ies.append(ies1)
        list_all_ies.append(ies2)
        list_all_ies.append(ies3)
        list_all_ies.append(ies4)
        list_all_ies.append(ies5)

        list_of_preenchimento_censo.append(
            self._construirPreenchimentoCenso(ies2))
        list_of_preenchimento_censo.append(
            self._construirPreenchimentoCenso(ies3))

        for censo in list_of_preenchimento_censo:
            alarm = any(censo.ies.name == x.name for x in list_all_ies)
            print(alarm)

        for ies in list_all_ies:
            alarm = any(
                ies.name == x.ies.name for x in list_of_preenchimento_censo)
            if alarm:
                print(ies.name + " Preenchou o Censo no ano de 2022")
            else:
                print(ies.name + " Não preencheou o Censo no ano de 2022")

    def _construirIES(self, name, number):
        return IES(name=name)

    def _construirPreenchimentoCenso(self, ies):
        return PreenchimentoCenso(ies=ies)
