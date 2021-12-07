from django.db import models

# Create your models here.
from django.contrib import admin
from django.db.models import Model

# TODO: Maybe add pretty print to each model for admin panel
class SkyscrapersPuzzle(models.Model):
	task = models.CharField(max_length=128, blank=False)
	solution = models.CharField(max_length=256, blank=False)
	difficulty = models.IntegerField(blank=False, default=0)


class User(models.Model):
	username = models.CharField(max_length=32)
	email = models.CharField(max_length=128)
	password = models.CharField(max_length=256)
	passwordSalt = models.CharField(max_length=16)
# TODO: Add puzzle history, maybe something like puzzleID, time taken to solve and... Link to replay?


class PlayedGame(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	puzzle = models.ForeignKey(SkyscrapersPuzzle, on_delete=models.CASCADE)
	date = models.DateTimeField()
	time = models.CharField(max_length=20)
