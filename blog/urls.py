from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.getMovieList, name='movie_list'),
	url(r'^movieList/$', views.getMovieList, name='mainPage'),
	url(r'^movie/detail/(?P<pk>\d+)$', views.movie_detail, name='movie_detail')
]