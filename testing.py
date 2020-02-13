# импорты
from bs4 import BeautifulSoup
import requests
"""
Написать парсер гораскопа 
"""
def connect(url):
    """
    Соеденияемя с сайтом
    :param url:
    :return: result
    """
    url = requests.get(url)
    if url.ok == True:
        result = url
    else:
        result = 'Проверь URL'
    return result


def get_data(url, zodiac_sing, topic):
    """
    распарсиваем гороскоп
    :param url: obj requests
    :param zodiac_sing: знак выбранного зодиака
    :param topic: тема гороскопа
    :return:
    """
    soup = BeautifulSoup(url.text, 'html5lib')
    return soup.find(zodiac_sing).find(topic).text



# Точка входа
if __name__ == '__main__':
    URL = 'https://ignio.com/r/export/utf/xml/weekly/cur.xml'
    r = connect(URL)
    z = get_data(r, zodiac_sing='aries', topic='business')
    print(z)