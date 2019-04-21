from base64 import b64encode
from io import BytesIO
from os.path import join

from django.conf import settings
from matplotlib import font_manager, rc, pyplot as plt


font_dirs = join(settings.BASE_DIR, 'assets/fonts')
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)

plt.rcParams['font.family'] = 'NanumGothicCoding'


def create_bar_plot(title, series):
    figure, ax = plt.subplots()
    figure.set_size_inches(15, 5)
    series.sort_values(ascending=True).plot.barh(ax=ax)
    ax.set_title(title)

    figfile = BytesIO()
    figure.savefig(figfile, format='png')
    chart_img = b64encode(figfile.getvalue()).decode('ascii')

    return chart_img

