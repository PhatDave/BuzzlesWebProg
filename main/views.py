import os
import random
import time
from datetime import datetime

from django.contrib.auth import *
from django.http import HttpResponseNotFound, \
	HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import main.ContextBuilder as cb
from main.models import *

languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	# return render(request, 'main/index.html', context)
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=('skyscrapers',)))


def GetRequestValue(request, val, default=0):
	try: return request.GET[val]
	except KeyError: return default


def GetSessionVal(request, val, default=0):
	try: return request.session[val]
	except KeyError: request.session[val] = default
	finally: return request.session[val]

# TODO: Ensure user does not get the same puzzle twice
# TODO: Leaderboard per puzzle with list of users which completed same puzzle


# noinspection PyTypeChecker
def gameDispatcher(request, puzzleName='skyscrapers', lang='en', diff=0, id=-1):
	# TODO: Rework this to work like userpage
	GetSessionVal(request, 'puzzleStart', str(time.mktime(datetime.now().timetuple())))
	if not IsValidGame(puzzleName):
		return HttpResponseNotFound()
	context = {}
	puzzleName = GetSessionVal(request, 'puzzleName', puzzleName)
	# TODO: What fucking retardation??????????????????????
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
		context['puzzleStart'] = request.session['puzzleStart']
		username = GetSessionVal(request, 'username', 'None')
		context['username'] = username
		return render(request, f'main/games/{puzzleName}.html', context)
	except KeyError as e:
		return HttpResponseNotFound()


def switchLang(request, lang):
	request.session['lang'] = lang
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'],]))


def switchDiff(request, diff):
	if diff != request.session['diff']:
		request.session['diff'] = diff
		request.session['puzzleID'] = -1
		request.session['puzzleStart'] = str(time.mktime(datetime.now().timetuple()))
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], ]))


def getNewPuzzle(request):
	request.session['puzzleID'] = -1
	request.session['puzzleStart'] = str(time.mktime(datetime.now().timetuple()))
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], ]))


def submitSolution(request):
	if request.user.is_authenticated:
		username = request.user.username
		puzzleID = request.POST['puzzleID']
		gameTime = request.POST['gameTimer']
		date = datetime.now()

		PlayedGame.objects.create(user=User.objects.get(username=username),
								  puzzle=SkyscrapersPuzzle.objects.get(id=puzzleID),
								  time=gameTime,
								  date=date)

		# TODO: Notify user about success
	return getNewPuzzle(request)


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


def userPage(request, username):
	user = User.objects.filter(username=username).get()
	if user is not None:
		context = {
			'user': user
		}
		return render(request, 'main/userPage.html', context=context)
	else:
		return HttpResponseRedirect(reverse('main:login'))


def siteLogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('main:login'))


def siteLogin(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage'))

	context = {
		'title': "Login"
	}
	return render(request, 'main/authentication/login.html', context)


def loginSubmit(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage'))

	email = request.POST['email']
	password = request.POST['password']

	user = authenticate(email=email, password=password)
	if user is None:
		user = authenticate(username=email, password=password)
	if user is None:
		context = {'loginFailed': request.POST['email']}
		return render(request, 'main/authentication/login.html', context)
	login(request, user)
	return HttpResponseRedirect(reverse('main:userPage'))


def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage'))

	context = {
		'title': "Register"
	}
	return render(request, 'main/authentication/register.html', context)


def registerSubmit(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage'))

	try:
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']

		EmailExists(email)
		UsernameExists(username)

		user = User.objects.create_user(email=email,
								 		username=username,
								 		password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('main:userPage'))
	except (KeyError, User.DoesNotExist, AssertionError) as e:
		context = {'error': "Unknown error"}
		return render(request, 'main/authentication/register.html', context)
	except (EmailExistsException, UsernameExistsException) as e:
		context = {'error': e.args[0]}
		return render(request, 'main/authentication/register.html', context)


def EmailExists(email):
	if User.objects.filter(email=email).__len__() > 0:
		raise EmailExistsException


def UsernameExists(username):
	if User.objects.filter(username=username).__len__() > 0:
		raise UsernameExistsException


class EmailExistsException(Exception):
	def __init__(self):
		super().__init__("Email already exists")


class UsernameExistsException(Exception):
	def __init__(self):
		super().__init__("Username already exists")


def GetModelFromName(puzzleName):
	if puzzleName == 'skyscrapers':
		return SkyscrapersPuzzle
	# elif puzzleName == 'futoshiki':
	# 	return FutoshikiPuzzle


def GetPuzzle(model, id=-1, diff=0):
	if id == -1:
		items = list(model.objects.filter(difficulty=diff).all())
		item = random.choice(items)
		return item
	else:
		pick = id
		puzzle = get_object_or_404(model, pk=pick, difficulty=diff)
		return puzzle