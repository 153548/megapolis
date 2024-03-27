from csv import DictReader, DictWriter

with open('history_mirror.csv', encoding='utf-8') as file:  # Открытие файла
    headers = ['date', 'username', 'verdict']
    data = list(DictReader(file, delimiter=','))

new_data = []
new_data.append(data[0])
for row in range(len(data)):

