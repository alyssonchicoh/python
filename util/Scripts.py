class Scripts:

    # CONSULTA TODOS OS PREENCHIMENTO DE CENSO DE UM ANO
    SCRIPT_01 = "SELECT * FROM fat_preenchimento_censo f1 inner join dim_ies ie on (f1.id_ies_fk = ie.id) WHERE date_part('year',f1.data_preenchimento) = #YEAR#"

    SCRIPT_02 = "INSERT INTO public.fat_alarme (data, data_correcao, status_correcao, severidade, tipo_indicador, desc_nome_indicador, versao_numero_indicador, nome_ies, radical_cnpj_ies, cnpj_ies, latitude_ies, longitude_ies, cidade_ies, estado_ies, endereco_ies, grupo_mantenedor_ies, ies_sede, nome_sede_ies, nome_curso, area_curso, carga_horaria_curso) VALUES(now(), null, #VALUE_1#, #VALUE_2#, #VALUE_3#, #VALUE_4#, #VALUE_5#, #VALUE_6#, #VALUE_7#, #VALUE_8#, #VALUE_9#, #VALUE_10#, #VALUE_11#, #VALUE_12#, #VALUE_13#, #VALUE_14#, #VALUE_15#, #VALUE_16#, #VALUE_17#, #VALUE_18#, #VALUE_19#);"

    # CONSULTA TODAS AS RENOVACOES AUTOMATICAS
    SCRIPT_03 = "select * from fat_renovacao_automatica fra left join dim_ies ies on (fra.id_ies_fk = ies.id) left join dim_curso c on (fra.id_curso_fk = c.id)"

    # CONSULTA TODAS AS RENOVACOES DADO UM ID DE IES
    SCRIPT_04 = "select * from fat_renovacao_automatica fra left join dim_ies ies on (fra.id_ies_fk = ies.id) left join dim_curso c on (fra.id_curso_fk = c.id) where fra.id_ies_fk = #VALUE_ID_IES#"

    def get_script(self, number, paramns):
        if (number == 1):
            return self._get_script_01(paramns)
        if (number == 2):
            return self._get_script_02(paramns)
        if (number == 3):
            return self._get_script_03(paramns)
        if (number == 4):
            return self._get_script_04(paramns)

    def _get_script_01(self, year):
        return self.SCRIPT_01.replace("#YEAR#", str(year))

    def _get_script_02(self, values):
        values = list(values.values())
        sql = self.SCRIPT_02
        for index, val in enumerate(values):
            tag = "#VALUE_"+str(index+1)+"#"
            value = str(val) if val != "" else "''"
            sql = sql.replace(tag, value)

        return sql

    def _get_script_03(self, value):
        return self.SCRIPT_03

    def _get_script_04(self, value):
        return self.SCRIPT_04.replace("#VALUE_ID_IES#", str(value))
