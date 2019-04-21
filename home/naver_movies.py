import re
import requests
from enum import Enum
from itertools import zip_longest
from urllib.parse import urljoin


class ChartType(Enum):
    예매순 = 'RESERVE'
    현재상영작 = 'CURRENT'
    다운로드 = 'DOWNLOAD'
    개봉예정작 = 'COMMING'
    평점순 = 'POINT'
    박스오피스 = 'BOXOFFICE'


def get_movie_detail(moive_code):
    params = {'code': moive_code}
    res = requests.get("https://movie.naver.com/movie/bi/mi/basic.nhn", params=params)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.mv_info_area .main_score .st_on')
    label_list = ['평점-관람객', '평점-평론가', '평점-네티즌']
    percent_list = []

    for tag in tag_list[:3]:
        matched = re.match(r'width:([\d\.]+)%', tag['style'])
        percent = '%.2f' % (float(matched.group(1)) / 10)
        percent_list.append(percent)

    return dict(zip_longest(label_list, percent_list, fillvalue=0))


def get_movie_chart(chart_type, include_detail=False):
    page_url = 'https://movie.naver.com/movieChartJson.nhn'
    params = {'type': chart_type.value}
    headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'),
        'Referer': 'https://movie.naver.com/',
    }
    res = requests.get(page_url, params=params, headers=headers)
    movie_list = res.json()['movieChartList'][chart_type.value]

    for movie in movie_list:
        detail_base_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
        movie['detailUrl'] = detail_base_url + '?code=' + str(movie['movieCode'])

        poster_host = 'https://movie-phinf.pstatic.net'
        poster_params = '?type=m203_290_2'
        movie['posterImageUrl'] = urljoin(poster_host, movie['posterImageUrl']) + poster_params

        if include_detail:
            detail = get_movie_detail(movie['movieCode'])
            movie.update(detail)
        yield movie

