import os

from django.http import HttpResponse
from django.shortcuts import render
import main.ContextBuilder as cb


languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def gameDispatcher(request, puzzleName):
	context = {}
	context = cb.BuildDefault(context)
	context = cb.Build(puzzleName, context)
	return render(request, 'main/game.html', context)


def login(request):
	context = {}
	return render(request, 'main/login.html', context)


def register(request):
	context = {}
	return render(request, 'main/register.html', context)