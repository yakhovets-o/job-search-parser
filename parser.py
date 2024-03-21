import csv
import time
import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from typing import Generator

from model import Vacancy


ua = UserAgent().random
HEADERS = {'User-Agent': ua}


def get_count_page(url: str, headers: dict) -> int | None:
    request = requests.get(url=url, headers=headers)
    if request.status_code != 200:
        return
    soup = BeautifulSoup(request.text, 'lxml')
    count_page = int(soup.find('div', class_='pager').find_all("a", class_='bloko-button')[-2].text)

    return count_page


def get_link(url: str, headers: dict) -> Generator[str, None, None] | None:
    count_page = get_count_page(url=URL, headers=HEADERS)

    for page in range(count_page):
        request = requests.get(url=url, headers=headers, params={'page': page})
        if request.status_code != 200:
            return

        soup = BeautifulSoup(request.text, 'lxml')
        links = soup.find_all('span', class_='serp-item__title-link-wrapper')

        for link in links:
            yield link.find("a", class_="bloko-link").get("href")

            time.sleep(1)


def get_vacancy(link: str, headers: dict) -> Vacancy | None:
    request = requests.get(url=link, headers=headers)

    if request.status_code != 200:
        return

    soup = BeautifulSoup(request.text, "lxml")
    try:
        job_title = soup.find('div', class_='vacancy-title').find('h1', class_='bloko-header-section-1').text
    except:
        job_title = 'Не указано'
    try:
        salary = soup.find('div', class_='vacancy-title'). \
            find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text
    except:
        salary = 'Не указана'
    try:
        work_experience = soup.find('p', class_='vacancy-description-list-item').text.split(': ')[1]
    except:
        work_experience = 'Не указан'
    try:
        work_format = soup.find_all('p', class_='vacancy-description-list-item')[-1].text
    except:
        work_format = 'Не указан'
    try:
        company_name = soup.find('span', class_='vacancy-company-name').text
    except:
        company_name = 'Не указан'
    try:
        key_skills = ', '.join(i.text.replace(' / ', ',     ') for i in
                               soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text'))
    except:
        key_skills = 'Не указаны'
    try:
        address = soup.find('span', attrs={'data-qa': 'vacancy-view-raw-address'}).text
    except AttributeError:
        address = 'Не указан'
    except:
        address = soup.find('p', attrs={'data-qa': 'vacancy-view-location'}).text

    return Vacancy(link=link,
                   job_title=job_title,
                   salary=salary,
                   work_experience=work_experience,
                   work_format=work_format,
                   company_name=company_name,
                   key_skills=key_skills,
                   address=address
                   )


def add_csv() -> None:
    create_csv()

    for link in get_link(url=URL, headers=HEADERS):
        vacancy = get_vacancy(link=link, headers=HEADERS)
        write_csv(vacancy=vacancy)


def create_csv() -> None:
    with open(file='vacancy.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'link',
            'job_title',
            'salary',
            'work_experience',
            'work_format',
            'company_name',
            'key_skills',
            'address'

        ])


def write_csv(vacancy: Vacancy) -> None:
    with open(file='vacancy.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            vacancy.link,
            vacancy.job_title,
            vacancy.salary,
            vacancy.work_experience,
            vacancy.work_format,
            vacancy.company_name,
            vacancy.key_skills,
            vacancy.address

        ])


if __name__ == '__main__':
    start = time.time()

    search_word = input('Введите Название профессии: ').capitalize()

    URL = f'https://rabota.by/search/vacancy?L_save_area=true&search_field=name&search_field=company_name&' \
          f'search_field=description&items_on_page=20&hhtmFrom=vacancy_search_filter&area=16&text={search_word}' \
          f'&enable_snippets=false'

    add_csv()
    finish = time.time()
    print(f'Время работы: {finish - start} sec')
