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


def GetRequestValue(request, val, default=0):
	try: return request.GET[val]
	except KeyError: return default


def GetSessionVal(request, val, default=0):
	try: return request.session[val]
	except KeyError: request.session[val] = default
	finally: return request.session[val]


# noinspection PyTypeChecker
def gameDispatcher(request, puzzleName='skyscrapers', puzzleID=0, lang='en', diff=0):
	GetSessionVal(request, 'puzzleStart', str(time.mktime(datetime.now().timetuple())))
	if not IsValidGame(puzzleName):
		return HttpResponseNotFound()

	context = {}
	puzzleName = GetSessionVal(request, 'puzzleName', puzzleName)
	# TODO: What fucking retardation??????????????????????
	# TODO: Use return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], request.session['puzzleID'], ]))
	# TODO: JS Async post req
	# TODO: https://api.jquery.com/jquery.post/
	# TODO: https://stackoverflow.com/questions/14642130/how-to-response-ajax-request-in-django/14642191
	if '.ico' in puzzleName:
		puzzleName = 'skyscrapers'
		request.session['puzzleName'] = puzzleName
	lang = GetSessionVal(request, 'lang', lang)
	diff = GetSessionVal(request, 'diff', diff)

	try:
		context = cb.BuildDefault(context)
		context = cb.Build(puzzleName,
						   lang=lang,
						   context=context,
						   diff=diff)

		# TODO: Check if ID is 0 ? Have new puzzle redirect to the correct URL and the dispatcher run again with good ID
		if puzzleID == 0:
			if request.session['puzzleID'] is None:
				return GetNewPuzzle(request)
			else:
				return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], request.session['puzzleID'], ]))
		puzzle = GetPuzzle(request, SkyscrapersPuzzle, puzzleID, diff)
		if GetSessionVal(request, 'puzzleID', puzzle.id) != puzzle.id:
			request.session['puzzleStart'] = str(time.mktime(datetime.now().timetuple()))
		request.session['puzzleID'] = puzzle.id

		context['puzzle'] = puzzle
		context['puzzleStart'] = request.session['puzzleStart']
		return render(request, f'main/games/{puzzleName}.html', context)
	except KeyError as e:
		return HttpResponseNotFound()


def GetPuzzle(request, model, id=0, diff=0):
	puzzle = model.objects.filter(id=id, difficulty=diff).get()
	return puzzle


def switchLang(request, lang):
	request.session['lang'] = lang
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], request.session['puzzleID'], ]))


def switchDiff(request, diff):
	if diff != request.session['diff']:
		request.session['diff'] = diff
		request.session['puzzleStart'] = str(time.mktime(datetime.now().timetuple()))
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], 0 ]))


def GetNewPuzzle(request):
	diff = GetSessionVal(request, 'diff', 0)
	user = request.user
	newPuzzle = GetRandomSkyscrapersPuzzle(diff, user)
	request.session['puzzleStart'] = str(time.mktime(datetime.now().timetuple()))
	# return newPuzzle
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=[request.session['puzzleName'], newPuzzle.id, ]))


def GetRandomSkyscrapersPuzzle(diff, user):
	userHistory = list(PlayedGame.objects.filter(user=user).all())
	puzzles = list(SkyscrapersPuzzle.objects.filter(difficulty=diff).all())
	filteredPuzzles = list(set(puzzles) - set(userHistory))
	puzzle = random.choice(filteredPuzzles)
	return puzzle


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
	return GetNewPuzzle(request)


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
		# This is hardcoded to skyscrapers for now, maybe TODO: rework for all puzzles?
		games = PlayedGame.objects.filter(user=user).all()
		context = {
			'games': games,
			'user': user,
			# TODO: Find a better way of doing this maybe?
			'puzzleID': request.session['puzzleID']
		}
		return render(request, 'main/userPage.html', context=context)
	else:
		return HttpResponseRedirect(reverse('main:login'))


def siteLogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('main:login'))


def siteLogin(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage', args=(request.user.username, )))

	context = {
		'title': "Login"
	}
	return render(request, 'main/authentication/login.html', context)


def loginSubmit(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage', args=(request.user.username, )))

	email = request.POST['email']
	password = request.POST['password']

	user = authenticate(email=email, password=password)
	if user is None:
		user = authenticate(username=email, password=password)
	if user is None:
		context = {'loginFailed': request.POST['email']}
		return render(request, 'main/authentication/login.html', context)
	login(request, user)
	return HttpResponseRedirect(reverse('main:gameDispatcher', args=('skyscrapers', 0, )))


def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage', args=(request.user.username, )))

	context = {
		'title': "Register"
	}
	return render(request, 'main/authentication/register.html', context)


def registerSubmit(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('main:userPage', args=(request.user.username, )))

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
		return HttpResponseRedirect(reverse('main:userPage', args=(request.user.username, )))
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


def gameLeaderboard(request, puzzleID):
	puzzle = SkyscrapersPuzzle.objects.filter(id=puzzleID).get()
	games = PlayedGame.objects.filter(puzzle=puzzle).all()
	context = {
		'puzzle': puzzle,
		'games': games,
		'puzzleID': request.session['puzzleID']
	}
	return render(request, 'main/gameLeaderboardPage.html', context=context)