import psycopg2


class DBConnector:

    def connect(self):
        con = psycopg2.connect(
            host='localhost',
            database='alarm_manager',
            user='postgres',
            password='postgres',
        )

        print("Conectado!")
        return con

    def search(self, sql):
        con = self.connect()
        cur = con.cursor()

        cur.execute(sql)
        recset = cur.fetchall()

        records = []

        for rec in recset:
            records.append(rec)

        con.close()

        return records

    def inserir(self, sql):
        con = self.connect()
        cur = con.cursor()

        try:
            cur.execute(sql)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            con.rollback()
            cur.close()
            return 1

        cur.close()
