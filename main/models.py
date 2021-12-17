from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.contrib import admin
from django.db.models import Model


class SkyscrapersPuzzle(models.Model):
	task = models.CharField(max_length=128, blank=False)
	solution = models.CharField(max_length=256, blank=False)
	difficulty = models.IntegerField(blank=False, default=0)

	def __str__(self):
		return str(self.id)

# class UserInfo(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return self.username


class PlayedGame(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	puzzle = models.ForeignKey(SkyscrapersPuzzle, on_delete=models.CASCADE)
	date = models.DateTimeField()
	time = models.CharField(max_length=20)

	def __str__(self):
		return f'{self.user.username}, {str(self.time)}, {self.puzzle.task}'
