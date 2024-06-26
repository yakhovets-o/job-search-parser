# :flower_playing_cards: Анализатор поиска работы
![Static Badge](https://img.shields.io/badge/Python-3.11-blue?style=flat)
![Static Badge](https://img.shields.io/badge/Beautiful%20Soup-4.12-black?style=flat)
![Static Badge](https://img.shields.io/badge/Requests-2.31-red?style=flat)
![Static Badge](https://img.shields.io/badge/Pandas%20-2.2-green?style=flat)
![Static Badge](https://img.shields.io/badge/Matplotlib-3.8-purple?style=flat)

---
## :wilted_flower: Описание

Анализатор  разработан для получения актуальной информации по вакансиям,  сохранением данных в файл и построением   диаграмм.

---
:evergreen_tree: Модуль ```scraper``` использует библиотеки:
* [***Requests***](https://requests.readthedocs.io/en/latest/index.html) - для HTTP запросов
* [***Beautiful Soup***](https://beautiful-soup-4.readthedocs.io/en/latest/) - для извлечения данных из HTML
* [***Fake-useragent***](https://fake-useragent.readthedocs.io/en/latest/) - для генерации случайного ```UserAgent```


Все данные записываются в файл формата ```csv```  [```vacancy.png```](https://github.com/yakhovets-o/job-search-parser/blob/main/vacancy.png)


---
:deciduous_tree: Модуль ```diagram``` использует библиотеки:
* [***Pandas***](https://pandas.pydata.org/pandas-docs/stable/index.html) - для анализа ```csv``` файла
* [***Matplotlib***](https://matplotlib.org/stable/index.html) - для визуализации

График сохраняется в файл [```skills_diagram.png```](https://github.com/yakhovets-o/job-search-parser/blob/main/skills_diagram.png)

---
:palm_tree: Модуль ```model``` содержит в себе ```dataclass```

---
## :desktop_computer: Установка
#### Для Windows
* Скопируйте репозиторий к себе на компьютер [***job-search-parser***](https://github.com/yakhovets-o/job-search-parser.git)
* Установите виртуальное окружение  ```python -m venv venv```
* Активируйте виртуальное окружение ```venv/Scripts/activate```
* Установите внешние библиотеки, выполнив: ```pip install -r requirements.txt```
* Запустите файл ```main.py```

---
## :sunflower: Лицензия 
Данный проект использует лицензию [***MIT***](https://github.com/yakhovets-o/job-search-parser/blob/main/LICENSE)


---
## :white_flower: Контакты 

Для связи в автором проекта писать на почту: yakhovetso@gmail.com








