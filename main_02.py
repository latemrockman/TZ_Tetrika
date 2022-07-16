import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pprint
import time

def counter_animals(url: str) -> dict:
    dict_animals = defaultdict(int)
    while True:
        # получаем список животных с текущей страницы:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        animals = soup.find('div', class_='mw-category mw-category-columns').find_all('li')

        # перебор текущего списка животных:
        for animal in animals:
            letter = animal.text[0]

            # проверка на русский язык, т.к. среди русских названий попалось одно английское:
            if letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                dict_animals[letter] += 1
                print(animal.text)

            # если буква 'A'(англ.), то заканчиваем и возвращаем результат:
            if letter == 'A':
                return dict_animals

        # получаем ссылку на следующую страницу:
        url = 'https://ru.wikipedia.org/' + soup.find('div', id='mw-pages').contents[7].attrs['href']
        #time.sleep(1)




# ссылка на исходую страницу:
url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90'

result = counter_animals(url)

print('\nРЕЗУЛЬТАТ:')
pprint.pprint(result, sort_dicts=False)




