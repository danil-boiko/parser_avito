
import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url) # получает url
    return r.text # возвращает текст html

#def get_total_pages(html):
    #soup = BeautifulSoup(html, 'lxml')

    #pages = soup.find('div', class_='pagination-pages').find_all('a', class_ = 'pagination-page')[-1].get('href') 
    # 1. находит нижний сайдбар
    # 2. фильтрует и оставляет только теги a (ссылки)
    # 3. возвращает последний элемент 

    #return int(total_pages)

def write_csv(data):
    with open('avito.csv', 'a', encoding='utf-8') as f:
      writer = csv.writer(f)

      writer.writerow((data['title'],
                       data['price'],
                       data['metro'],
                       data['url']) )  

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_ = 'catalog-list').find_all('div', class_ = 'item_table')
    # ищет блок с объявлениями и фильтрует их

    for ad in ads: # для каждого объявления в списке
        # title, price, metro, url
        name = ad.find('div', class_ = 'description').find('h3').text.strip().lower()

        if 'htc' in name:

            try:
                title = ad.find('div', class_ = 'description').find('h3').text.strip()
                # получает заголовок в объявлении
            except:
                title = ''
            
            try:
                url ='https://www.avito.ru' + ad.find('div', class_ = 'description').find('h3').find('a').get('href')
                # получает ссылку на товар
            except:
                url = ''
            
            try:
                price = ad.find('div', class_ = 'about').text.strip().split('₽')[0].strip()
                # получает цену
            except:
                price = ''

            try:
                metro = ad.find('div', class_ = 'data').find_all('p')[-1].text.strip()
                # получает метро
            except:
                metro = ''
                
            data = {'title': title,
                    'price': price,
                    'metro': metro,
                    'url': url} 

            write_csv(data)
        else:
            continue


def main():
    url = 'https://www.avito.ru/sankt-peterburg/telefony?p=1&q=htc'
    base_url = 'https://www.avito.ru/sankt-peterburg/telefony?'
    page_part = 'p=' # часть страницы
    query_part = '&q=htc' # часть запроса

    # total_pages = get_total_pages(get_html(url)) # получает количество страниц 

    for i in range(1, 3): # цикл перебирает страницы, при желании вмеcто 3 поставить total_pages
        url_gen = base_url + page_part +str(i) + query_part
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)




if __name__ == '__main__':
    main()

