import datetime
import openpyxl


class XlsxHandler:
    """
    Получаем все строки из страницы
    :return generator: итерируемый объект вида [[Строка № 1], [Строка № 2]]
    """
    def __init__(self, full_path):
        self.full_path = full_path
        self.book = openpyxl.load_workbook(self.full_path)
        self.sheet = self.book.worksheets[0]

    def caller(self):
        if self.full_path == "Федеральная ОСК.xlsx":
            self.final = self.osk_fed()
            self.book.close()
            return self.final
        elif self.full_path == "АДМ-Практика.xlsx":
            self.final = self.adm_praktika()
            self.book.close()
            return self.final
        elif self.full_path == "АБД-Центр.xlsx":
            self.final = self.abd_centre()
            self.book.close()
            return self.final
        elif self.full_path == "Запретники.xlsx":
            self.final = self.zapret()
            self.book.close()
            return self.final
        elif self.full_path == "Региональная ОСК.xlsx":
            self.final = self.osk_reg()
            self.book.close()
            return self.final
        elif self.full_path == "Федеральный розыск.xlsx":
            self.final = self.fed_roz()
            self.book.close()
            return self.final
        else:
            print('caller: другие функции не реализованы')

    def rows_handler(self):
        for row in self.sheet.iter_rows():
            yield [cell.value for cell in row]

    def osk_fed(self):
        """
        Обработка таблицы "Федеральная ОСК"
        """
        generator = self.rows_handler()
        self.final_list = []
        for elem in list(generator):
            # убираем первую ячейку с порядковым номером
            elem_truncated = elem[1:]
            if type(elem_truncated[4]) is datetime.datetime:
                elem_truncated[4] = elem_truncated[4].strftime('%d.%m.%Y')
            if elem_truncated[0] is None:
                break
            else:
                self.final_list.append([tuple(elem_truncated)])
        # убираем заголовочную строку [1:]
        #print(f'DEBUG def osk_fed() final_list -> {len(self.final_list[1:])}')
        return self.final_list[1:]

    def adm_praktika(self):
        """
        Обработка таблицы "АДМ-Практика"
        """
        generator = self.rows_handler()
        self.final_list = []
        for elem in list(generator):
            # убираем первую ячейку с порядковым номером
            elem_truncated = elem[1:]
            # проверяем поле "Дата рождения"
            if type(elem_truncated[4]) is datetime.datetime:
                elem_truncated[4] = elem_truncated[4].strftime('%d.%m.%Y')
            # проверяем поле "Дата постановления"
            #print(type(elem_truncated[16]))
            if type(elem_truncated[16]) is datetime.datetime:
                elem_truncated[16] = elem_truncated[16].strftime('%d.%m.%Y')
            if elem_truncated[0] is None:
                break
            else:
                self.final_list.append([tuple(elem_truncated)])
        # убираем заголовочную строку [1:]
        #print(f'DEBUG def adm_praktika() final_list -> {self.final_list}')
        return self.final_list[1:]

    def abd_centre(self):
        """
        Обработка таблицы "АБД-Центр"
        """
        generator = self.rows_handler()
        self.final_list = []
        for elem in list(generator):
            # убираем первую ячейку с порядковым номером
            elem_truncated = elem[1:]
            # проверяем поле "Дата рождения"
            if type(elem_truncated[4]) is datetime.datetime:
                elem_truncated[4] = elem_truncated[4].strftime('%d.%m.%Y')
            if elem_truncated[0] is None:
                break
            else:
                self.final_list.append([tuple(elem_truncated)])
        # убираем заголовочную строку [1:]
        #print(f'DEBUG def abd_centre() final_list -> {self.final_list}')
        return self.final_list[1:]

    def zapret(self):
        """
        Обработка таблицы "Запретники
        """
        generator = self.rows_handler()
        self.final_list = []
        for elem in list(generator):
            # убираем первую ячейку с порядковым номером
            elem_truncated = elem[1:]
            # проверяем поле "Дата рождения"
            if type(elem_truncated[4]) is datetime.datetime:
                elem_truncated[4] = elem_truncated[4].strftime('%d.%m.%Y')
            if elem_truncated[0] is None:
                break
            else:
                self.final_list.append([tuple(elem_truncated)])
        # убираем заголовочную строку [1:]
        #print(f'DEBUG def zapret() final_list -> {self.final_list}')
        return self.final_list[1:]

    def osk_reg(self):
        """
        Обработка таблицы "Региональная ОСК"
        """
        generator = self.rows_handler()
        self.final_list = []
        for elem in list(generator):
            # убираем первую ячейку с порядковым номером
            elem_truncated = elem[1:]
            # проверяем поле "Дата рождения"
            if type(elem_truncated[4]) is datetime.datetime:
                elem_truncated[4] = elem_truncated[4].strftime('%d.%m.%Y')
            if elem_truncated[0] is None:
                break
            else:
                self.final_list.append([tuple(elem_truncated)])
        # убираем заголовочную строку [1:]
        #print(f'DEBUG def reg_osk() final_list -> {self.final_list}')
        return self.final_list[1:]

    def fed_roz(self):
        """
        Обработка таблицы "Федеральный розыск"
        """
        generator = self.rows_handler()
        self.final_list = []
        for elem in list(generator):
            # убираем первую ячейку с порядковым номером
            elem_truncated = elem[1:]
            # проверяем поле "Дата рождения"
            if type(elem_truncated[4]) is datetime.datetime:
                elem_truncated[4] = elem_truncated[4].strftime('%d.%m.%Y')
            if elem_truncated[0] is None:
                break
            else:
                self.final_list.append([tuple(elem_truncated)])
        # убираем заголовочную строку [1:]
        #print(f'DEBUG def list_incoming() final_list -> {self.final_list}')
        return self.final_list[1:]


if __name__ == '__main__':
    pass