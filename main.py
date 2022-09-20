from user_interaction import Questions
from excel import XlsxHandler
from db import DBConnect

DEBUG = True

class Manager:
    def __init__(self):
        question = Questions()
        if DEBUG: print(f'DEBUG: question -> {question}')

        xlsx = XlsxHandler(question.path + question.file_name)
        ban_list = xlsx.caller()
        if DEBUG: print(f'DEBUG: ban_list -> {ban_list}')

        db = DBConnect()
        if DEBUG: print(f'DEBUG: db -> {db}')

        db.query_osk_fed(ban_list, question.date)
        db.con_close()


if __name__ == '__main__':
    program = Manager()