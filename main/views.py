import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
import main.ContextBuilder as cb
from main.models import *

languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def gameDispatcher(request, lang='en', puzzleName='skyscrapers'):
	context = {}
	try: diff = request.GET['diff']
	except KeyError: diff = 0
	try:
		context = cb.BuildDefault(context)
		context = cb.Build(puzzleName,
						   lang=lang,
						   context=context,
						   diff=diff)
		puzzle = get_object_or_404(SkyscrapersPuzzle, pk=1)
		context = cb.AddTaskAndSolution(context, puzzle)
		return render(request, f'main/games/{puzzleName}.html', context)
	except KeyError as e:
		return HttpResponseNotFound()


def login(request):
	context = {}
	return render(request, 'main/login.html', context)


def register(request):
	context = {}
	return render(request, 'main/register.html', context)