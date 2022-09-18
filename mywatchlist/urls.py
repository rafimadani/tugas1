from django.urls import path
from mywatchlist.views import show_movies_html
from mywatchlist.views import show_movies_xml
from mywatchlist.views import show_movies_json



app_name = 'mywatchlist'

urlpatterns = [
    path('htmlview/', show_movies_html, name='show_movies_html'),
    path('xml/', show_movies_xml, name='show_movies_xml'),
    path('json/', show_movies_json, name='show_movies_json'),
]