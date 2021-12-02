import os

from django.http import HttpResponse
from django.shortcuts import render


puzzleDifficulties = {
	"/skyscrapers/": [
		"4x4 Easy",
		"4x4 Normal",
		"4x4 Hard",
		"5x5 Easy",
		"5x5 Normal",
		"5x5 Hard",
		"6x6 Easy",
		"6x6 Normal",
		"6x6 Hard",
	]
}
languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def skyscrapers(request):
	context = {"diffs": puzzleDifficulties[request.path], "langs": languageIcons}
	return render(request, 'main/skyscrapers.html', context)