from django.db import models

# Create your models here.

class Tweet(models.Model):
	author = models.ForeignKey('Auth.User')
	message = models.CharField(max_length = 160)
	date_created = models.DateTimeField('date created')
	slug = models.SlugField(max_length = 50)

class Retweet(models.Model):
	retweeted_message = models.ForeignKey(Tweet)
	date_retweeted = models.DateTimeField('default date')

class Reply(models.Model):
	replier = models.ForeignKey('Auth.User')
	message = models.ForeignKey(Tweet)
	replied_message = models.CharField(max_length = 160)
	reply_date = models.DateTimeField('default date')
