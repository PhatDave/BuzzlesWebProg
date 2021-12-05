import os
import random

from django.http import HttpResponse, HttpResponseNotFound, \
	HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import main.ContextBuilder as cb
from main.models import *

languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def switchLang(request, lang):
	request.session['lang'] = lang
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'],]))


def switchDiff(request, diff):
	request.session['diff'] = diff
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'],]))


def GetRequestValue(request, val, default=0):
	try: return request.GET[val]
	except KeyError: return default


def GetSessionVal(request, val, default=0):
	try: return request.session[val]
	except KeyError: request.session[val] = default
	finally: return request.session[val]


def gameDispatcher(request, puzzleName='skyscrapers', lang='en', diff=0):
	context = {}
	puzzleName = GetSessionVal(request, 'puzzleName', puzzleName)
	lang = GetSessionVal(request, 'lang', lang)
	diff = GetSessionVal(request, 'diff', diff)

	model = GetModelFromName(puzzleName)
	try:
		context = cb.BuildDefault(context)
		context = cb.Build(puzzleName,
						   lang=lang,
						   context=context,
						   diff=diff)
		puzzle = GetPuzzle(model, diff=diff)
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


def GetModelFromName(puzzleName):
	if puzzleName == 'skyscrapers':
		return SkyscrapersPuzzle


def GetPuzzle(model, id=-1, diff=0):
	if id == -1:
		last = model.objects.filter(difficulty=diff).last().id
		pick = random.randint(1, last)
	puzzle = get_object_or_404(model, pk=pick, difficulty=diff)
	return puzzle