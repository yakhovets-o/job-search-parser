# Анализатор поиска работы
![Static Badge](https://img.shields.io/badge/Python-3.11-blue?style=flat)
![Static Badge](https://img.shields.io/badge/Beautiful%20Soup-4.12-black?style=flat)
![Static Badge](https://img.shields.io/badge/Requests-2.31-red?style=flat)
![Static Badge](https://img.shields.io/badge/Pandas%20-2.2-green?style=flat)
![Static Badge](https://img.shields.io/badge/Matplotlib-3.8-purple?style=flat)

---
## Описание

Анализатор  разработан для получения актуальной информации по вакансиям,  сохранением данных в файл и составлением  диаграммы.

---
Модуль ```parser``` использует библиотеки:
* [***Requests***](https://requests.readthedocs.io/en/latest/index.html) - для HTTP запросов
* [***Beautiful Soup***](https://beautiful-soup-4.readthedocs.io/en/latest/) - для извлечения данных из HTML
* [***Fake-useragent***](https://fake-useragent.readthedocs.io/en/latest/) - для генерации случайного ```UserAgent```


Все данные записываются в файл формата ```csv```

![2024-03-21_20-33-19](https://github.com/yakhovets-o/job-search-parser/assets/112704107/0f6f8b73-1d9f-4df0-afb0-d5e98e8c0d3c)


---
Модуль ```diagram``` использует библиотеки:
* [***Pandas***](https://pandas.pydata.org/pandas-docs/stable/index.html) - для анализа ```csv``` файла
* [***Matplotlib***](https://matplotlib.org/stable/index.html) - для визуализации


![2024-03-21_20-48-43](https://github.com/yakhovets-o/job-search-parser/assets/112704107/0677573b-6676-4530-8d76-e83bcb9b5fd0)


---
Модуль ```model``` содержит в себе ```dataclass```


---
## Лицензия 
Данный проект использует лицензию [***MIT***](https://github.com/yakhovets-o/job-search-parser/blob/main/LICENSE)


---
## Контакты 

Для связи в автором проекта писать на почту: yakhovetso@gmail.com







