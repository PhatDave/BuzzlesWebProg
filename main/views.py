import os

from django.http import HttpResponse
from django.shortcuts import render
import main.ContextBuilder as cb


puzzleDifficulties = {
	"/skyscrapers/": [
	]
}
languageIcons = os.listdir('main/static/main/imgs/lang')


def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def skyscrapers(request):
	context = {
		"diffs": puzzleDifficulties[request.path],
		"langs": languageIcons
	}
	context = cb.BuildSkyscrapers(context)
	return render(request, 'main/skyscrapers.html', context)