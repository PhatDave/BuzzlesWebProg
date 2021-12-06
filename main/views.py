import os
import random
import hashlib
import string

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


def userPage(request):
	context = {}
	if GetSessionVal(request, 'userName', None) is not None:
		return render(request, 'main/userPage.html')
	else:
		return HttpResponseRedirect(reverse('main:login'))


def login(request):
	context = {
		'title': "Login"
	}
	if GetSessionVal(request, 'userName', None) is not None:
		return HttpResponseRedirect(reverse('main:userPage'))
	return render(request, 'main/login.html', context)


# TODO: Encode passwords w base64 and then hash?; to make sure special characters don't explode
def loginSubmit(request):
	try:
		# TODO: Also check for username (for authentication) in case email fails
		user = User.objects.get(email=request.POST['email'],
								 password=request.POST['password'])
	except (KeyError, User.DoesNotExist) as e:
		# TODO: Deal with this context in html for failed login
		context = {'loginFailed': request.POST['email']}
		return render(request, 'main/login.html', context)


def register(request):
	context = {
		'title': "Register"
	}
	return render(request, 'main/register.html', context)


def registerSubmit(request):
	context = {}
	try:
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']

		# TODO: do something better later
		# assert len(password) > 0
		# assert len(email) > 0
		EmailExists(email)
		UsernameExists(username)

		m = hashlib.sha3_256()
		salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
		m.update(password.encode('utf-8'))
		m.update(salt.encode('utf-8'))
		hashedPassword = m.hexdigest()
		User.objects.create(email=email, password=hashedPassword,
							username=username, passwordSalt=salt)
	except (KeyError, User.DoesNotExist, AssertionError) as e:
		context = {'error': "Unknown error"}
	except (EmailExistsException, UsernameExistsException) as e:
		context = {'error': e.message}
	finally:
		return render(request, 'main/register.html', context)


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


def GetPuzzle(model, id=-1, diff=0):
	if id == -1:
		items = list(model.objects.filter(difficulty=diff).all())
		item = random.choice(items)
		return item
	else:
		pick = id
		puzzle = get_object_or_404(model, pk=pick, difficulty=diff)
		return puzzle