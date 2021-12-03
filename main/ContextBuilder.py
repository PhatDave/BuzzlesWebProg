from main.Localization import *

locals = Localization()


def BuildSkyscrapers(context, lang='en'):
	for i, (k, v) in enumerate(locals.content['Skyscrapers'][lang].items()):
		context[k] = v
	return context


def BuildDefault(context):
	return context
