import requests
from bs4 import BeautifulSoup

start_num = 1
for i in range(100):
    url = f'https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=38&start={start_num}&refresh_start=0'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    li_list = soup.select('#wrap > #container > #content > div.main_pack > section.sc_new > div.api_subject_bx > div.group_news > ul.list_news > li')

    for li in li_list:
        print(li.select_one('div.news_wrap.api_ani_send > div.news_area > a').get("title"))
        print(li.select_one('div.news_wrap.api_ani_send > div.news_area > a').get("href"))
    
    print()
    start_num += 10
    