import json
import os

from main.Localization import *

locals = Localization()


def Build(puzzleName, context, lang='en', diff=0):
	for i, (k, v) in enumerate(locals.content[puzzleName][lang].items()):
		context[k] = v
	context = AddPuzzleSize(context, puzzleName, diff)
	return context


def BuildDefault(context):
	context = AddPuzzles(context)
	context = AddFlags(context)
	return context


def AddPuzzles(context):
	context['puzzleGameIcons'] = []
	for i in os.listdir('main/static/main/imgs/games'):
		fName = i.split('.')[0]
		context['puzzleGameIcons'].append({"img": i, "name": fName, "lowerName": fName.lower()})
	return context


def AddFlags(context):
	context['langFlags'] = []
	for i in os.listdir('main/static/main/imgs/lang'):
		fName = i.split('.')[0]
		context['langFlags'].append({"img": i, "name": fName, "lowerName": fName.lower()})
	return context


def AddPuzzleSize(context, pName, pDiff):
	if pName == 'skyscrapers':
		if pDiff < 3:
			context['pSize'] = 4
			context['pSizeArray'] = [i for i in range(4)]
		elif pDiff < 6:
			context['pSize'] = 5
			context['pSizeArray'] = [i for i in range(5)]
		else:
			context['pSize'] = 6
			context['pSizeArray'] = [i for i in range(6)]
	return context


def AddTaskAndSolution(context, puzzle):
	task = puzzle.task.split('/')
	solution = puzzle.solution.split('/')
	puzzleSize = int(len(task) / 4)
	context['task'] = {
		"top": task[:puzzleSize],
		"bottom": task[puzzleSize:puzzleSize * 2],
		"left": task[puzzleSize * 2:puzzleSize * 3],
		"right": task[puzzleSize * 3:puzzleSize * 4],
	}
	context['solution'] = solution
	context['taskJ'] = "/".join(task)
	context['solutionJ'] = "/".join(solution)
	return context