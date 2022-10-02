from user_interaction import Questions
from excel import XlsxHandler
from db import DBConnect, DBInfo

DEBUG = False


class Manager:
    def __init__(self):
        # Получаем адрес клиента и сведения для подключения в СУБД
        settings_db = DBInfo()
        client_path = settings_db.settings["client_path"]
        connection = settings_db.settings["connection"]
        if DEBUG: print(f'DEBUG: settings_db -> {settings_db.settings}')

        # Получаем ответ от пользователя на вопрос о выборе файла для обработки
        question = Questions()
        if DEBUG: print(f'DEBUG: question -> {question}')

        # Обрабатываем xlsx файл
        xlsx = XlsxHandler(question.path + question.file_name)
        ban_list = xlsx.caller()
        if DEBUG: print(f'DEBUG: ban_list -> {ban_list}')

        # Выполняем загрузку в таблицу БД списка лиц
        db = DBConnect(question.path + question.file_name, ban_list, question.date, client_path, connection)
        if DEBUG: print(f'DEBUG: db -> {db}')

        db.caller()
        db.con_close()
        if DEBUG: print(f'DEBUG: DEBUG: db -> {db}, question.date -> {question.date}')


if __name__ == '__main__':
    program = Manager()
    input('для выхода из программы нажмите enter: ')