import cx_Oracle
import json


class DBConnect:
    """
    Реализуется подключение к СУБД
    """
    def __init__(self, full_path, ban_list, question_date, ora_client, connection):
        self.full_path = full_path
        self.ban_list = ban_list
        self.question_date = question_date
        self.ora_client = ora_client
        cx_Oracle.init_oracle_client(lib_dir=self.ora_client)
        self.connection = cx_Oracle.connect(connection)
        self.cursor = self.connection.cursor()

    def caller(self):
        if self.full_path == "Федеральная ОСК.xlsx":
            self.query_osk_fed(self.ban_list, self.question_date)
        elif self.full_path == "АДМ-Практика.xlsx":
            self.query_adm_praktika(self.ban_list, self.question_date)
        elif self.full_path == "АБД-Центр.xlsx":
            self.query_abd_centre(self.ban_list, self.question_date)
        elif self.full_path == "Запретники.xlsx":
            self.query_zapret(self.ban_list, self.question_date)
        elif self.full_path == "Региональная ОСК.xlsx":
            self.query_osk_reg(self.ban_list, self.question_date)
        elif self.full_path == "Федеральный розыск.xlsx":
            self.query_fed_roz(self.ban_list, self.question_date)
        else:
            print('caller: другие функции не реализованы')

    def query_osk_fed(self, ban_list, question_date):
        self.sql = f"insert into pribyl_oskf (fam, imj, otch, dt_rojd, mes_rojd, info, dt_v) values (:1, :2, :3, :4, :5, :6, :7)"
        self.cursor.prepare(self.sql)
        #self.inf = [('test', 'test', 'test', '10.10.2022', 'test', 'test', question_date)]
        #self.cursor.executemany(None, self.inf)
        print('Список загруженных записей: ')
        for b in ban_list:
            self.cursor.prepare(self.sql)
            b[0] = b[0] + (question_date,)
            print(b[0])
            self.cursor.executemany(None, b)
        print('Количество загруженных записей', len(ban_list))
        self.connection.commit()

    def query_adm_praktika(self, ban_list, question_date):
        self.sql = f"insert into pribyl_adm_2 " \
                   f"(FAM, IMJ, OTCH, DT_ROJD, DT_SOVER, STATUS, ORGAN, ADRES, GLAVA, STATJA, PART, ITEM, KODEX, XAR_NAR, NAKAZ, DATA_POSTAN, FABULA, DT_V) " \
                   f"values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18)"
        self.cursor.prepare(self.sql)
        #self.inf = [('test', 'test', 'test', '10.10.2022', 'test', 'test', question_date)]
        #self.cursor.executemany(None, self.inf)
        print('Список загруженных записей: ')
        for b in ban_list:
            self.cursor.prepare(self.sql)
            b[0] = b[0] + (question_date,)
            print(b[0])
            self.cursor.executemany(None, b)
        print('Количество загруженных записей', len(ban_list))
        self.connection.commit()

    def query_abd_centre(self, ban_list, question_date):
        self.sql = f"insert into PRIBYL_ABDC " \
                   f"(FAM, IMJ, OTCH, DT_ROJD, MES_ROJD, PASP, REGION, VID_DOC, N_DOC, DT_DOC, STATJA, VID_PRE, DT_RESH, RESH, FABULA, DT_V) " \
                   f"values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16)"
        self.cursor.prepare(self.sql)
        #self.inf = [('test', 'test', 'test', '10.10.2022', 'test', 'test', question_date)]
        #self.cursor.executemany(None, self.inf)
        print('Список загруженных записей: ')
        for b in ban_list:
            self.cursor.prepare(self.sql)
            b[0] = b[0] + (question_date,)
            print(b[0])
            self.cursor.executemany(None, b)
        print('Количество загруженных записей', len(ban_list))
        self.connection.commit()

    def query_zapret(self, ban_list, question_date):
        self.sql = f"insert into PRIBYL_ZAPR " \
                   f"(FAM, IMJ, OTCH, DT_ROJD, GRAJD, VID_D, DT_V) " \
                   f"values (:1, :2, :3, :4, :5, :6, :7)"
        self.cursor.prepare(self.sql)
        #self.inf = [('test', 'test', 'test', '10.10.2022', 'test', 'test', question_date)]
        #self.cursor.executemany(None, self.inf)
        print('Список загруженных записей: ')
        for b in ban_list:
            self.cursor.prepare(self.sql)
            b[0] = b[0] + (question_date,)
            print(b[0])
            self.cursor.executemany(None, b)
        print('Количество загруженных записей', len(ban_list))
        self.connection.commit()

    def query_osk_reg(self, ban_list, question_date):
        self.sql = f"insert into PRIBYL_OSKR " \
                   f"(FAM, IMJ, OTCH, DT_ROJD, MES_ROJD, REGION, INFO, DT_V) " \
                   f"values (:1, :2, :3, :4, :5, :6, :7, :8)"
        self.cursor.prepare(self.sql)
        #self.inf = [('test', 'test', 'test', '10.10.2022', 'test', 'test', question_date)]
        #self.cursor.executemany(None, self.inf)
        print('Список загруженных записей: ')
        for b in ban_list:
            self.cursor.prepare(self.sql)
            b[0] = b[0] + (question_date,)
            print(b[0])
            self.cursor.executemany(None, b)
        print('Количество загруженных записей', len(ban_list))
        self.connection.commit()

    def query_fed_roz(self, ban_list, question_date):
        self.sql = f"insert into PRIBYL_FR " \
                   f"(FAM, IMJ, OTCH, DT_ROJD, MES_ROJD, PASP, INO_DOC, N_INO_DOC, INIC_ROZ, KATEG, INIC_ROZ_OVD, STATJA, UK, MERA_PRES, N_CIRKUL, DT_OBJAV, OS_PRIM, DT_PREKR, CONTACT, N_CIRKUL_P, DT_V) " \
                   f"values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21)"
        self.cursor.prepare(self.sql)
        #self.inf = [('test', 'test', 'test', '10.10.2022', 'test', 'test', question_date)]
        #self.cursor.executemany(None, self.inf)
        print('Список загруженных записей: ')
        for b in ban_list:
            self.cursor.prepare(self.sql)
            b[0] = b[0] + (question_date,)
            print(b[0])
            self.cursor.executemany(None, b)
        print('Количество загруженных записей', len(ban_list))
        self.connection.commit()

    def con_close(self):
        self.cursor.close()
        self.connection.close()

    def __repr__(self):
        return f'cx_Oracle version: {cx_Oracle.version}'


class DBInfo:
    def __init__(self):
        with open("settings.json", "r") as file:
            self.settings = json.load(file)