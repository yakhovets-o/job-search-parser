import time

from scraper import add_csv
from diagram import building_diagram


def main():
    start = time.time()
    add_csv()
    finish = time.time()
    print(f'Время работы: {finish - start} sec')

    building_diagram()


if __name__ == '__main__':
    main()
