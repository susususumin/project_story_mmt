from django.db import models
from django.utils import timezone

class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length = 150)
	text = models.TextField()
	Created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title
		
class Movie(models.Model):
	"""docstring for Post"""
	director = models.CharField(max_length = 40)
	movieTitle = models.CharField(max_length = 150)
	city = models.CharField(max_length = 40)
	country = models.CharField(max_length = 40)
	place = models.CharField(max_length = 150)
	caption = models.TextField()
	Created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.movieTitle

# Create your models here.
