from bs4 import BeautifulSoup as bs
import requests

rq = requests.get('https://pt.wikipedia.org/wiki/Toy_Story_3')

soup = bs(rq.content, 'lxml')

contents = soup.prettify()

info_box = soup.find(class_ = 'infobox infobox_v2')

movie_info = {}

for index, row in enumerate(info_box.find_all("tr")):
    if index == 0:
        movie_info['title'] = row.find('th').get_text()
    elif index == 1:
        continue
    elif index == 2:
        movie_info['Country'] = row.find_all('a')[0].get_text()
        movie_info['Year'] = row.find_all('a')[1].get_text()
    else:
        content_key = row.find('th').get_text()
        content_value = row.find('td').get_text()
        movie_info[content_key] = content_value