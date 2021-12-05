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
	if diff != request.session['diff']:
		request.session['diff'] = diff
		request.session['puzzleID'] = -1
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'],]))


def getNewPuzzle(request):
	request.session['puzzleID'] = -1
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'],]))


def GetRequestValue(request, val, default=0):
	try: return request.GET[val]
	except KeyError: return default


def GetSessionVal(request, val, default=0):
	try: return request.session[val]
	except KeyError: request.session[val] = default
	finally: return request.session[val]


def gameDispatcher(request, puzzleName='skyscrapers', lang='en', diff=0, id=-1):
	# LoadPuzzlesFromFile()
	if not IsValidGame(puzzleName):
		return HttpResponseNotFound()
	context = {}
	puzzleName = GetSessionVal(request, 'puzzleName', puzzleName)
	# What fucking retardation??????????????????????
	if '.ico' in puzzleName:
		puzzleName = 'skyscrapers'
		request.session['puzzleName'] = puzzleName
	lang = GetSessionVal(request, 'lang', lang)
	diff = GetSessionVal(request, 'diff', diff)
	id = GetSessionVal(request, 'puzzleID', id)

	model = GetModelFromName(puzzleName)
	try:
		context = cb.BuildDefault(context)
		context = cb.Build(puzzleName,
						   lang=lang,
						   context=context,
						   diff=diff)
		puzzle = GetPuzzle(model, id=id, diff=diff)
		request.session['puzzleID'] = puzzle.id
		context = cb.AddTaskAndSolution(context, puzzle)
		return render(request, f'main/games/{puzzleName}.html', context)
	except KeyError as e:
		return HttpResponseNotFound()

def IsValidGame(puzzleName):
	model = GetModelFromName(puzzleName)
	if model is None:
		return False
	return True


def LoadPuzzlesFromFile():
	for diff in [0, 3, 6]:
		tasks = []
		solutions = []
		with open(f"{diff}tasks.txt", 'r') as f:
			tasks = f.readlines()
		with open(f"{diff}solutions.txt", 'r') as f:
			solutions = f.readlines()
		for i, v in enumerate(tasks):
			SkyscrapersPuzzle.objects.create(task=tasks[i][:-1], solution=solutions[i][:-1], difficulty=diff)


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
		items = list(model.objects.filter(difficulty=diff).all())
		item = random.choice(items)
		return item
	else:
		pick = id
		puzzle = get_object_or_404(model, pk=pick, difficulty=diff)
		return puzzle