import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.test import Client
from .models import Movie
from .models import Post



# Create your views here.


def getMovieList(request) : 
	movies = Movie.objects.order_by('-movieTitle')
	context = {'movies' : movies}
	return render(request, 'blog/movie_list.html',context)

def post_list(request) :
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})

def place(request, Movie) : 
	response = request.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=AIzaSyC6SFUxL15xJfjnJSwXnOOZECisoo7PemI',getMovieList.Movie.place)
	jsonData = json.loads(response)
	photo_url = ("//maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=%s?key=AIzaSyC6SFUxL15xJfjnJSwXnOOZECisoo7PemI",jsonData.photos.photo_reference)
	return HttpResponse(photo_url)


def search(request, content) :
	movies = Movie.objects.filter(contains=content)
	context = {'movies' : movie}
	return render(request, 'blog/mainPage.html',context)

class AboutUs(TemplateView) :
    template_name = 'blog/about.html'

from .models import Movie

class MovieDetail(TemplateView) :
    template_name = 'blog/movie_detail.html'

    def movie_detail(request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, 'blog/movie_detail.html', {'movie': movie}, {'url': MovieDetail.find_place(request, pk)})

    def getJasonResponse(selfrequest):
        return JsonResponse({'key': "value"})

    def find_place(request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        struct = {"refernece": "data"}
        response = {}
        c = Client()

        response = request.GET.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=AIzaSyC6SFUxL15xJfjnJSwXnOOZECisoo7PemI', movie.place)
        struct = json.loads(response)
        print(struct)
        photo_url = ("//maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=%s?key=AIzaSyC6SFUxL15xJfjnJSwXnOOZECisoo7PemI",struct.photos.photo_reference)
        return photo_url





