from csv import DictReader, DictWriter

with open('history_mirror.csv', encoding='utf-8') as file:  # Открытие файла
    headers = ['date', 'username', 'verdict']
    data = list(DictReader(file, delimiter=','))

data_error = []
for row in data:
    if row['verdict'] == 'Победа над смертью':  # Поиск человека с соответствующим предсказанием
        data_error.append({'date': row['date'], 'username': row['username']})

with open('mirror_error_test.csv', 'w', encoding='utf-8') as file:  # Запись подходящего человека в отдельный файл 'mirror_error_test.csv'
    writer = DictWriter(file, fieldnames=['date', 'username'], delimiter=',', lineterminator='\n')
    writer.writeheader()
    writer.writerows(data_error)

dates = [[i['date'], i['username']] for i in data_error]
dates = sorted(dates)  #Сортировка подходящих строк по дате
man = dates[0][1].split()
print(f"Сообщение было зафиксировано: {dates[0][0]} у пользователя {man[0]} {man[1][0]}.{man[2][0]}.")
