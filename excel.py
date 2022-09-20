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
        elif self.full_path == "1":
            print('caller: другие функции не реализованы')
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
            if type(elem[3]) is datetime.datetime:
                elem[3] = elem[3].strftime('%d.%m.%Y')
            if elem[0] is None:
                break
            else:
                self.final_list.append([tuple(elem)])
        # пропускаем заголовочную строку [1:]
        return self.final_list[1:]


if __name__ == '__main__':
    pass