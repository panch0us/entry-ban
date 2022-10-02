class Questions:
    """
    Вопросы для пользователя
    """

    def __init__(self, path=''):
        self.date_input()
        self.file_name_input()
        self.path_ipnut(path)

    def date_input(self):
        # Если go = 2 программа продолжает просить корректно ввести дату, если 1 = завершается успешно
        go = '2'
        while go == '2':
            self.date = str(input('Введите дату файла в формате дд.мм.гггг: '))
            if len(self.date) == 10:
                print(f'Введена дата: {self.date}')
                go = self.rechek()
            else:
                print('Дата не соответсвует указанному формату!')
                go = '2'
        return self.date

    def file_name_input(self):
        files_names = {
            '1': 'Федеральная ОСК.xlsx',
            '2': 'АДМ-Практика.xlsx',
            '3': 'АБД-Центр.xlsx',
            '4': 'Запретники.xlsx',
            '5': 'Региональная ОСК.xlsx',
            '6': 'Федеральный розыск.xlsx',
        }
        # Если go = 2 программа продолжает просить корректно ввести дату, если 1 = завершается успешно
        go = '2'
        while go == '2':
            for key in files_names:
                print(f'{key} -> {files_names[key]}')
            file = str(input(f'Введите № файла для обработки: '))
            if file == '1':
                print(f'Выбран файл: "Федеральная ОСК.xlsx"')
                go = self.rechek()
            elif file == '2':
                print(f'Выбран файл: "АДМ-Практика.xlsx"')
                go = self.rechek()
            elif file == '3':
                print(f'Выбран файл: "АБД-Центр"')
                go = self.rechek()
            elif file == '4':
                print(f'Выбран файл: "Запретники"')
                go = self.rechek()
            elif file == '5':
                print(f'Выбран файл: "Региональная ОСК"')
                go = self.rechek()
            elif file == '6':
                print(f'Выбран файл: "Федеральный розыск"')
                go = self.rechek()
            else:
                print('Выбран неподходящий номер, попробуйте ещё!')
                go = '2'
        self.file_name = files_names[file]
        return self.file_name

    def path_ipnut(self, path=''):
        self.path = path
        return self.path

    def rechek(self):
        """
        Перепроверка подтверждения пользователя
        :return: str '1' or '2'
        """
        go = '0'
        while go != '1' or go != '2':
            go = str(input('Продолжить? (1 - да, 2 - исправить): '))
            if go == '1' or go == '2':
                break
            else:
                print('Значение не соответсвует указанному формату!')
                go = '0'
        return go

    def __repr__(self):
        if len(self.path) > 0:
            return f'Дата: {self.date}, Путь: {self.path}, Имя файла: "{self.file_name}".'
        else:
            return f'Дата: "{self.date}", Путь: "Текущая директория", Имя файла: "{self.file_name}".'


if __name__ == '__main__':
    question = Questions()
    print('Результат: ', question)