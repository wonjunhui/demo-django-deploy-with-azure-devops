import pandas as pd
from django.shortcuts import render
from .naver_movies import ChartType, get_movie_chart
from .utils import create_bar_plot


def index(request):
    movie_list = get_movie_chart(ChartType.예매순)
    movie_df = pd.DataFrame(movie_list).set_index('movieTitle')
    chart_img = create_bar_plot('예매율 차트', movie_df.reserveRatio)

    return render(request, 'home/index.html', {
        'movie_df': movie_df,
        'chart_img': chart_img,
    })

