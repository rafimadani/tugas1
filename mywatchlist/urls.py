from django.urls import path
from mywatchlist.views import show_movies_html
from mywatchlist.views import show_movies_xml
from mywatchlist.views import show_movies_json
from mywatchlist.views import show_movies_json_id
from mywatchlist.views import show_movies_xml_id




app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_movies_html, name='show_movies_html'),
    path('xml/', show_movies_xml, name='show_movies_xml'),
    path('json/', show_movies_json, name='show_movies_json'),
    path('json/<int:id>', show_movies_json_id, name='show_json_by_id'),
    path('xml/<int:id>', show_movies_xml_id, name='show_xml_by_id'),
]