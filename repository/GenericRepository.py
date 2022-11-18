from repository.DBConnector import DBConnector
from utils.SQLGenerator import SQLGenerator


class GenericRepository():

    def insert(self, table, values):
        db = DBConnector()
        db.inserir(SQLGenerator.generator_sql_insert(table, values))

    def search_all(self, table):
        db = DBConnector()
        return db.search(SQLGenerator.generator_sql_search_all(table))

    def search_by_id():
        pass

    def search_all_with_inner_join(self, main_table, secondary_table,
                                   fk_main_table, id_secondary_table):
        db = DBConnector()
        return db.search(SQLGenerator.generator_sql_search_all_with_inner_join(main_table, secondary_table,
                                                                               fk_main_table, id_secondary_table))
