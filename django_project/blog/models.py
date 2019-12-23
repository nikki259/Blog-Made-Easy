from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	# date_posted = models.DateTimeField(auto_now_add=True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	keywords = models.TextField(default='keywords')
	text_summary = models.TextField(default='blog summary')
	#image = models.ImageField(default='images.jfif',blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})


class Blog(models.Model):
	title = models.CharField(max_length= 150)
	content = models.TextField()
	dateposted = models.DateTimeField(default=timezone.now)
	auth = models.ForeignKey(User,on_delete=models.CASCADE)


	def __str__(self):
		return self.title

class Blogthis(models.Model):
	title = models.CharField(max_length= 150)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	keywords = models.TextField()
	auth = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title



class BlogImage(models.Model):
	img = models.ForeignKey(Blog,on_delete=models.CASCADE)
	image = models.ImageField(default='images.jfif',upload_to='blog_images/')


class BlogImageAgain(models.Model):
	img = models.ForeignKey(Post,on_delete=models.CASCADE)
	image = models.ImageField(default='images.jfif',upload_to='blog_images_again/')
