import requests
from bs4 import BeautifulSoup

response = requests.get('https://movie.naver.com/movie/running/current.nhn')

html = response.text
soup = BeautifulSoup(html, 'html.parser')
movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

movies_list = []
for movie in movies:
    title = movie.select_one('dl > dt > a').text
    code = movie.select_one(' dl > dt > a')['href'].split('?code=')[1]
    # print({'title: {0}, code: {1}'.format(movie.select_one('dl > dt > a').text, movie.select_one(' dl > dt > a')['href'][28:])})
    movie_data = {'title': f'{title}', 'code': f'{code}'}
    movies_list.append(movie_data)


for movie in movies_list:
    code = movie['code']
    title = movie['title']
    for i in range(1,20):
        headers = {
            'authority': 'movie.naver.com',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'iframe',
            'referer': 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189075&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'NNB=NARNWDHTZFTWA; nx_ssl=2; _gihttps://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189075&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2d=GA1.2.905442669.1618223909; ASID=7db24df000000178c69b5baa00000053; notSupportBrowserAlert=true; BMR=s=1618377670987&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dwideeyed%26logNo%3D221350638501%26proxyReferer%3Dhttps%3A%252F%252Fwww.google.com%252F&r2=https%3A%2F%2Fwww.google.com%2F; _ga_7VKFYR6RV1=GS1.1.1618382417.21.0.1618382417.60; _ga=GA1.2.1482821382.1617416898; csrf_token=0fe6638e-6f38-408f-8094-1ea860bc1147',
        }

        params = (
            ('code', f'{code}'),
            ('type', 'after'),
            ('isActualPointWriteExecute', 'false'),
            ('isMileageSubscriptionAlready', 'false'),
            ('isMileageSubscriptionReject', 'false'),
            ('page', f'{i}')
        )
        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        comments = soup.select('body > div > div > div.score_result > ul > li')
        page_num = 0
        for comment in comments:
            print(title)
            print('평점: {}'.format(comment.select_one('div.star_score > em').text))
            if comment.select_one((f'div.score_reple > p > #_filtered_ment_{page_num} > span.unfold_ment')):
                print(comment.select_one(f'div.score_reple > p > #_filtered_ment_{page_num} > span > a')['data-src'], '\n')    
            else:
                print(comment.select_one(f'div.score_reple > p > #_filtered_ment_{page_num}').text.strip(),'\n')
            page_num += 1


