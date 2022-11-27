import csv
from util.DBConnector import DBConnector
import csv
from util.GenericRepository import GenericRepository



class ImportData:
    @staticmethod
    def generateCSV():
        generic_repository = GenericRepository()

        sql = ""
        sql = sql + "SELECT "
        sql = sql + "       ID," #0
        sql = sql + "       to_char(data,'dd/MM/yyyy'), " #1
        sql = sql + "       data_correcao, " #2
        sql = sql + "       status_correcao," #3
        sql = sql + "       severidade," #4
        sql = sql + "       tipo_indicador," #5
        sql = sql + "       desc_nome_indicador," #6
        sql = sql + "       versao_numero_indicador," #7
        sql = sql + "       valor_corrente," #8
        sql = sql + "       valor_anterior," #9
        sql = sql + "       nome_ies," #10
        sql = sql + "       radical_cnpj_ies," #11
        sql = sql + "       cnpj_ies," #12
        sql = sql + "       latitude_ies," #13
        sql = sql + "       longitude_ies," #14
        sql = sql + "       cidade_ies," #15
        sql = sql + "       estado_ies," #16
        sql = sql + "       endereco_ies," #17
        sql = sql + "       grupo_mantenedor_ies," #18
        sql = sql + "       ies_sede," #19
        sql = sql + "       nome_sede_ies," #20
        sql = sql + "       nome_curso," #21
        sql = sql + "       area_curso," #22
        sql = sql + "       carga_horaria_curso" #23
        sql = sql + " from public.fat_alarme "

        alarmes = generic_repository.search_by_sql(sql);

        with open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/alarmes_reais.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "PK_ALARME",
                    "DATA_HORA_ALARME",
                    "DATA_CORRECAO",
                    "NATUREZA_JURIDICA",
                    "NATUREZA_JURIDICA_SIMPLIFICADA",
                    "STATUS_CORRECAO",
                    "SEVERIDADE",
                    "TIPO_INDICADOR",
                    "DSC_NOME_INDICADOR",
                    "VERSAO_NUMERO_INDICADOR",
                    "NOME_IES",
                    "RADICAL_CNPJ_IES",
                    "CNPJ_IES",
                    "LATITUDE",
                    "LONGITUDE",
                    "ESTADO",
                    "REGIAO",
                    "CIDADE",
                    "ENDEREÇO",
                    "GRUPO",
                    "MANTENEDOR",
                    "IES_SEDE",
                    "OME_SEDE",
                    "NOME_CURSO",
                    "AREA_CURSO",
                    "CARGA_HORARIA_CURSO"
                 ]
            )


            for alarme in alarmes:
                writer.writerow(
                    [
                        alarme[0], # PK_ALARME
                        alarme[1], # DATA_HORA_ALARME
                        alarme[2], # DATA_CORRECAO
                        '', # NATUREZA_JURIDICA
                        '', # NATUREZA_JURIDICA_SIMPLIFICADA
                        alarme[3], # STATUS_CORRECAO
                        'MEDIO', # SEVERIDADE
                        alarme[5], # TIPO_INDICADOR
                        alarme[6], # DSC_NOME_INDICADOR
                        alarme[7], # VERSAO_NUMERO_INDICADOR
                        alarme[10], # NOME_IES
                        alarme[11], # RADICAL_CNPJ_IES
                        alarme[12], # CNPJ_IES
                        alarme[13], # LATITUDE
                        alarme[14], # LONGITUDE
                        alarme[16], # ESTADO
                        '', # REGIAO
                        alarme[15], # CIDADE
                        alarme[17], # ENDEREÇO
                        alarme[18], # GRUPO
                        alarme[18], # MANTENEDOR
                        alarme[19], # IES_SEDE
                        alarme[21], # NOME_CURSO
                        alarme[22], # AREA_CURSO
                        alarme[23], # CARGA_HORARIA_CURSO
                    ]
                )

    @staticmethod
    def run():
        instituicoes = {}
        ficheiro = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/dados.csv', 'rt')
        reader = csv.reader(ficheiro)
        for line in reader:
            linhaFormatada = str(line).split(";")
            instituicoes[str(linhaFormatada[0].replace('[', '').replace("'", ''))] = str(linhaFormatada[1])

        for key, value in instituicoes.items():
            print("insert into dim_ies (id,nome) values (" + str(key) + ",'" + str(value).replace("'",' ') + "');")

    @staticmethod
    def run2():
        ficheiro = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/dados.csv', 'rt')
        arquivo = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/cursos.sql', 'w')

        reader = csv.reader(ficheiro)
        i = 0
        db = DBConnector()

        for line in reader:
            if i > 0:
                linhaFormatada = str(line).split(";")
                sql = "INSERT INTO DIM_CURSO (ID,NOME,AREA,ID_IES_FK) values (#VALUE_A#,#VALUE_B#,#VALUE_C#,#VALUE_D#);"

                sql = sql.replace("#VALUE_A#", str(linhaFormatada[2]))
                sql = sql.replace("#VALUE_B#", "'" + str(linhaFormatada[3]).replace("'", ' ') + "'")
                sql = sql.replace("#VALUE_C#", "'" + str(linhaFormatada[4]).replace("'", ' ') + "'")
                sql = sql.replace("#VALUE_D#", str(linhaFormatada[0].replace('[', '').replace("'", '')))

                db.inserir(sql);
                print("salvo")
            i = i + 1
        arquivo.close()
        print("fim")

    @staticmethod
    def run_preenchimento_censo():
        ficheiro = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/preenchimento_censo.csv', 'rt')
        reader = csv.reader(ficheiro)
        i = 0
        db = DBConnector()
        for line in reader:
            if i > 0:
                linhaFormatada = str(line).split(";")

                sql = "insert into fat_preenchimento_censo (id,data_preenchimento,id_ies_fk) values (#VALOR_A#,'01-01-#VALOR_B#',#VALOR_C#)"
                sql = sql.replace("#VALOR_A#", str(linhaFormatada[0].replace('[', '').replace("'", '')))
                sql = sql.replace("#VALOR_B#", str(linhaFormatada[1].replace('[', '').replace("'", '')))
                sql = sql.replace("#VALOR_C#", str(linhaFormatada[2].replace('[', '').replace("'", '')))
                sql = sql.replace("#VALOR_D#", str(linhaFormatada[3].replace(']', '').replace("'", '')))
                db.inserir(sql)
                print(sql)

            i = i + 1
        print("fim")
    @staticmethod
    def run_renovacao_automatica():
        ficheiro = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/renovacoes_automaticas.csv', 'rt')
        reader = csv.reader(ficheiro)
        i = 0
        db = DBConnector()
        for line in reader:
            if i > 0:
                linhaFormatada = str(line).split(";")

                sql = "INSERT INTO public.fat_renovacao_automatica (data_renovacao, sequencial_de_tipo, id_ies_fk, id_curso_fk) VALUES('#VALUE_A#', 0, #VALUE_C#, #VALUE_D#);"
                sql = sql.replace("#VALUE_A#", str(linhaFormatada[5].replace(']', '').replace("'", '')))
                sql = sql.replace("#VALUE_B#", str(linhaFormatada[4].replace('[', '').replace("'", '')))
                sql = sql.replace("#VALUE_C#", str(linhaFormatada[0].replace('[', '').replace("'", '')))
                sql = sql.replace("#VALUE_D#", str(linhaFormatada[2].replace(']', '').replace("'", '')))
                db.inserir(sql)
                print(sql)

            i = i + 1
        print("fim")

    @staticmethod
    def run_enderecos():
        ficheiro = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/enderecos.csv', 'rt')
        reader = csv.reader(ficheiro)
        i = 0
        db = DBConnector()
        for line in reader:
            linhaFormatada = str(line).split(";")
            sede = str(linhaFormatada[14]).upper()
            if sede.__contains__("S"):
                sql = "UPDATE DIM_IES SET cidade = '#VALUE_A#',estado = '#VALUE_B#',endereco = '#VALUE_C#',latitude = '#VALUE_D#',longitude = '#VALUE_E#' where id = #VALUE_F#";
                sql = sql.replace("#VALUE_A#",str(linhaFormatada[6]).replace("'", ''))
                sql = sql.replace("#VALUE_B#", str(linhaFormatada[5]).replace("'", ''))
                sql = sql.replace("#VALUE_C#", str(linhaFormatada[9].replace("'", '')) + ","+ str(linhaFormatada[10]).replace("'", ''))
                sql = sql.replace("#VALUE_D#", str(linhaFormatada[12]).replace("'", ''))
                sql = sql.replace("#VALUE_E#", str(linhaFormatada[13]).replace("'", ''))
                sql = sql.replace("#VALUE_F#", str(linhaFormatada[0].replace('[', '').replace("'", '')).replace("'", ''))
                db.inserir(sql)
                print(sql)
            i = i + 1
        print("fim2")

    @staticmethod
    def run_cnpj():
        ficheiro = open('/Users/alyssonchicoh/Documents/mac/alarm_manager/util/cnpjs.csv', 'rt')
        reader = csv.reader(ficheiro)
        i = 0
        db = DBConnector()
        for line in reader:
            linhaFormatada = str(line).split(";")
            sql = "update dim_ies set cnpj = '#VALUE_A#' where id = #VALUE_B#";
            sql = sql.replace("#VALUE_A#", str(linhaFormatada[3]).replace("'", ''))
            sql = sql.replace("#VALUE_B#", str(linhaFormatada[0].replace('[', '').replace("'", '')).replace("'", ''))
            db.inserir(sql)
            print(sql)
            i = i + 1
        print("fim2")
