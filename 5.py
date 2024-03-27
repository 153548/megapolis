from csv import DictReader, DictWriter

with open('history_mirror.csv', encoding='utf-8') as file:  # Открытие файла
    headers = ['date', 'username', 'verdict']
    data = list(DictReader(file, delimiter=','))

p = 67
m = 10 ** 9 + 9


def get_hash(name):
    """Функция предназначена для вычисления хэша по ФИО


        Описание аргументов:
        name - ФИО человека
    """

    h = 0
    for index in range(len(name)):
        h += ord(name[index]) * p ** index  # Вычисление хэша

    return h % m


for index_man in range(len(data)):  # Присваивание хэша каждому человеку
    data[index_man] = {'ID': get_hash(data[index_man]['username']), 'date': data[index_man]['date'],
                       'username': data[index_man]['username'], 'verdict': data[index_man]['verdict']}

with open('users_with_hash.csv', 'w', encoding='utf-8') as file:  # Запись информации в новый файл
    writer = DictWriter(file, fieldnames=['ID'] + headers, delimiter=',', lineterminator='\n')
    writer.writeheader()
    writer.writerows(data)
