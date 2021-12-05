from django.urls import path

from main.views import *

app_name = 'main'
urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('switchLang/<str:lang>', switchLang, name="switchLang"),
    path('switchDiff/<int:diff>', switchDiff, name="switchDiff"),
    path('getNewPuzzle', getNewPuzzle, name="getNewPuzzle"),

    path('<str:puzzleName>/', gameDispatcher, name="gameDispatcher"),
]
