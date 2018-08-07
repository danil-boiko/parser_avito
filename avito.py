
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url) # получает url
    return r.text # возвращает текст html

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_ = 'pagination-page')[-1].get('href') 
    # 1. находит нижний сайдбар
    # 2. фильтрует и оставляет только теги a (ссылки)
    # 3. возвращает последний элемент 

    total_pages = pages.split('=')[1].split('&')[0] # получает колличество страниц                                                                                        

    return int(total_pages)

def main():
    url = 'https://www.avito.ru/sankt-peterburg/telefony?p=1&q=htc'
    base_url = 'https://www.avito.ru/sankt-peterburg/telefony?'
    page_part = 'p=' # часть страницы
    query_part = '&q=htc' # часть запроса

    total_pages = get_total_pages(get_html(url)) # получает количество страниц 

    for i in range(1, total_pages): # цикл перебирает страницы
        url_gen = base_url + page_part +str(i) + query_part
        print(url_gen)




if __name__ == '__main__':
    main()

