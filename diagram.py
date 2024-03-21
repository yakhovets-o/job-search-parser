import csv
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

'''Открываем файл при помощи менеджера контекста
DictReader для отображения информации о каждой строке в качестве словаря'''

with open(file='vacancy.csv', mode='r', encoding='utf-8') as file:
    vacancy = csv.DictReader(file, delimiter=',')

    '''Получаем список ключевых навыков Counter это класс для подсчета хеш-объектов'''
    key_skills = Counter(
        skill.strip().replace(u'\xa0', u' ').capitalize() for row in vacancy if row['key_skills'] for skill in
        row['key_skills'].split(',')).most_common(15)

'''Создание DataFrame'''

df = pd.DataFrame(key_skills, columns=['key_skills', 'count'])

'''Цвета для использования в круговой диаграмме.'''

colors = [
    'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple',
    'Pink', 'Brown', 'Gray', 'Violet', 'Indigo', 'Magenta',
    'Cyan', 'Teal', 'Lavender'
]
'''Заголовок к круговой диаграмме'''

title = 'Key skills in vacancies'

'''Определите соотношение зазоров каждого фрагмента в кортеже'''

explode = (0.05,) * 15

'''autopct = '%1.0f%%' Отображает проценты на круговой диаграмме.
kind='pie' Тип диаграммы
y='count' значения использоваться для определения размера сегментов диаграммы.'''

df.groupby(['key_skills']).sum().plot(
    kind='pie', y='count', autopct='%1.0f%%',
    colors=colors, explode=explode, title=title)

'''loc='lower right' указывает на то, что легенда будет расположена в нижнем правом углу графика.
bbox_to_anchor=(0, 0) определяет точное местоположение легенды она будет расположена в самом нижнем правом углу.'''

plt.legend(loc='lower right', bbox_to_anchor=(0, 0))

''''skills.png' - это имя файла, в который будет сохранен график. 
Формат файла определяется по расширению, в данном случае .png указывает на то,
что график будет сохранен в формате PNG.
bbox_inches='tight' - этот параметр обеспечивает, чтобы вокруг графика не было лишнего пространства.
'tight' автоматически уменьшает размер холста, чтобы он соответствовал размерам графика.'''

plt.savefig('skills_diagram.png', bbox_inches='tight')
plt.show()
plt.close()