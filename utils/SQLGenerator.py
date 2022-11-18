# CLASSE UTILITARIA PARA GERAÇÃO DE SCRIPTS SQL
class SQLGenerator:

    TEMPLATE_SQL_INSERT = "INSERT INTO #TABLE# (#FIELDS#) VALUES (#VALUES#)"
    TEMPLATE_SQL_SEARCH_ALL = "SELECT * FROM #TABLE#"
    TEMPLATE_SQL_SEARCH_ALL_WITH_INNER_JOIN = "SELECT * FROM #TABLE_A# T1 INNER JOIN #TABLE_B# T2 ON (T1.#ID_A# = T2.#ID_B#)"

    @staticmethod
    def generator_sql_insert(table, values):
        fields_and_values = SQLGenerator._build_fields_and_values(values)

        sql = SQLGenerator.TEMPLATE_SQL_INSERT

        sql = sql.replace("#TABLE#", table)
        sql = sql.replace("#TABLE#", table)
        sql = sql.replace("#FIELDS#", fields_and_values[0])
        sql = sql.replace("#VALUES#", fields_and_values[1])

        return sql

    @staticmethod
    def generator_sql_search_all(table):

        sql = SQLGenerator.TEMPLATE_SQL_SEARCH_ALL
        sql = sql.replace("#TABLE#", table)

        return sql

    @staticmethod
    def generator_sql_search_all_with_inner_join(main_table, secondary_table,
                                                 fk_main_table, id_secondary_table):
        sql = SQLGenerator.TEMPLATE_SQL_SEARCH_ALL_WITH_INNER_JOIN
        sql = sql.replace("#TABLE_A#", main_table)
        sql = sql.replace("#TABLE_B#", secondary_table)
        sql = sql.replace("#ID_A#", fk_main_table)
        sql = sql.replace("#ID_B#", id_secondary_table)

        return sql

    def generator_sql_delete():
        pass

    def generator_sql_update():
        pass

    # CONSTRO AS COLUNAS E OS VALORES PARA O SQL DE INSERT
    # RETORNA UMA LISTA
    # ITEM 1 = NOME DAS COLUNAS
    # ITEM 2 = VALORES DOS CAMPOS

    @staticmethod
    def _build_fields_and_values(values):
        values_return = []
        sql_fields = ""
        sql_values = ""

        for key in values:
            if (key != "id"):
                sql_fields = sql_fields + key + ","
                sql_values = sql_values + \
                    SQLGenerator._build_field(values[key]) + ","

        values_return.append(sql_fields[:-1])
        values_return.append(sql_values[:-1])

        return values_return

    # CONSTROI O FORMATO DO CAMPO SQL COM BASE EM SEU TIPO
    @staticmethod
    def _build_field(value):
        return str(value) if isinstance(value, int) else str("'"+value+"'")
