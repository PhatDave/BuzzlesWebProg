from django.db import models

# Create your models here.
from django.contrib import admin
from django.db.models import Model


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