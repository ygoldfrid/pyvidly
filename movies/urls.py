from django.urls import path
from . import views

app_name = 'movies'

# movies/
urlpatterns = [
    # movies/
    path('', views.index, name='index'),
    # movies/id
    path('<int:movie_id>', views.detail, name='detail'),
]
