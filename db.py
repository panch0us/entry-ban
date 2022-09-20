import cx_Oracle
import json


class DBConnect:
    """
    Реализуется подключение к СУБД
    """
    def __init__(self):
        self.ora_client = r"I:\windows 10\Program Files\instantclient_11_2"
        cx_Oracle.init_oracle_client(lib_dir=self.ora_client)
        self.connection = cx_Oracle.connect("name/password@ip:1521/sid")
        self.cursor = self.connection.cursor()

    def query_osk_fed(self, ban_list, question_date):
        self.sql = f"insert into pribyl_oskf (fam, imj, otch, dt_rojd, mes_rojd, info, dt_v) values (:1, :2, :3, :4, :5, :6, :7)"
        self.cursor.prepare(self.sql)
        for b in ban_list:
            b[0] = b[0] + (question_date,)
            print(b)
            self.cursor.executemany(None, b)
        self.connection.commit()

    def con_close(self):
        self.cursor.close()
        self.connection.close()

    def __repr__(self):
        return f'cx_Oracle version: {cx_Oracle.version}'
