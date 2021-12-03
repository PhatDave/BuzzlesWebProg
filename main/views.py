import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import main.ContextBuilder as cb


languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def gameDispatcher(request, lang='en', puzzleName='skyscrapers'):
	request.session['lang'] = lang
	context = {}
	try:
		context = cb.BuildDefault(context)
		context = cb.Build(puzzleName, lang=lang, context=context)
		return render(request, f'main/games/{puzzleName}.html', context)
	except KeyError as e:
		return HttpResponseNotFound()


def login(request):
	context = {}
	return render(request, 'main/login.html', context)


def register(request):
	context = {}
	return render(request, 'main/register.html', context)