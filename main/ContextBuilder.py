import os

from main.Localization import *

locals = Localization()


def Build(puzzleName, context, lang='en'):
	for i, (k, v) in enumerate(locals.content[puzzleName][lang].items()):
		context[k] = v
	return context


def BuildDefault(context):
	context = AddPuzzles(context)
	context = AddFlags(context)
	return context


def AddPuzzles(context):
	context['puzzleGameIcons'] = []
	for i in os.listdir('main/static/main/imgs/games'):
		fName = i.split('.')[0]
		context['puzzleGameIcons'].append({"img": i, "name": fName})
	return context


def AddFlags(context):
	context['langFlags'] = []
	for i in os.listdir('main/static/main/imgs/lang'):
		fName = i.split('.')[0]
		context['langFlags'].append({"img": i, "name": fName})
	return context