import os
import pandas as pd
from django.conf import settings
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


def debug(request):
    hidden_fields = ['AZURE', 'AWS', 'TOKEN', 'API']
    skip_fields = ['CONDA', 'FLAG']

    def get_environment_varialbes():
        for k, v in os.environ.items():
            for name in hidden_fields:
                if name in k.upper():
                    v = v[:3] + '*' * (len(v) - 3)
                    break

            if any(name for name in skip_fields if name in k.upper()):
                continue

            yield (k, v)

    return render(request, 'home/debug.html', {
        'settings': settings,
        'environment_variables': get_environment_varialbes(),
    })

