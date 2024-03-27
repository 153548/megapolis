from csv import DictReader

with open('history_mirror.csv', encoding='utf-8') as file:  # Открытие файла
    headers = ['date', 'username', 'verdict']
    data = list(DictReader(file, delimiter=','))

years = [0] * 24  # Создание 24 года с кол-вом записей для каждого года
for man in data:  # Распределение записей по годам
    date = man['date'].split('-')
    year = int(date[0])
    years[year-2000] += 1

for year in range(24):  # Вывод
    print(f"В {year+2000} году зеркало было использовано {years[year]}.")