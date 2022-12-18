from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('movies/',views.movies, name='movies'),
    path('tv_shows/',views.tv_shows, name='tv_shows'),
    re_path('movie/(\d+)', views.single_movie, name='single_movie'),
    re_path('tv_show/(\d+)',views.single_tv_show, name='single_tv_show'),
    path('search',views.search,name='search'),
]