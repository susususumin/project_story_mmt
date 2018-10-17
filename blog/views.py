from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Movie
import requests
import json



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

def movie_detail(request, pk) : 
	movie = get_object_or_404(Movie, pk=pk)
	return render(request, 'blog/movie_detail.html', {'movie' : movie})