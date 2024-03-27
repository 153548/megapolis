from csv import DictReader


def get_info(names):
    """Функция предназначена для поиска предсказания по имени и отчеству.

    Описание аргументов:
    names - имя и отчество человека либо кодовое слово 'stop' для завершения программ

    """

    if names == 'stop':  # Проверка на кодовое слово 'stop'
        return False
    names = names.split()  # Разбивка имени и отчества на отдельные строки
    for man in data:  # Поиск соответствующего человека
        if man['username'].split()[1] == names[0] and man['username'].split()[2] == names[1]:
            print(f"Предсказание для {man['username'].split()[0]} {man['username'].split()[1][0]}"
                  f".{man['username'].split()[2][0]}. - {man['verdict']}")
            return True
    print('Вас не нашлось в записях')
    return True


with open('history_mirror.csv', encoding='utf-8') as file:  # Открытие файла
    headers = ['date', 'username', 'verdict']
    data = list(DictReader(file, delimiter=','))  # Разбиение строк на разные группы

flag = True
while flag:
    name = input()
    flag = get_info(name)
