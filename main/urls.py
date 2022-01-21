from django.urls import path

from main.views import *

app_name = 'main'
urlpatterns = [
    path('userPage/<str:username>/', userPage, name="userPage"),
    path('gameLeaderboard/<int:puzzleID>', gameLeaderboard, name='gameLeaderboard'),
    path('login/', siteLogin, name="login"),
    path('logout/', siteLogout, name="logout"),
    path('loginSubmit/', loginSubmit, name="loginSubmit"),

    path('register/', register, name="register"),
    path('registerSubmit/', registerSubmit, name="registerSubmit"),

    path('switchLang/<str:lang>/', switchLang, name="switchLang"),
    path('switchDiff/<int:diff>/', switchDiff, name="switchDiff"),
    path('getNewPuzzle/', GetNewPuzzle, name="getNewPuzzle"),
    path('submitSolution/', submitSolution, name="submitSolution"),

    path('<str:puzzleName>/<int:puzzleID>/<int:diff>', gameDispatcher, name="gameDispatcher"),
    path('<str:puzzleName>/<int:puzzleID>/', gameDispatcher, name="gameDispatcher"),
    path('<str:puzzleName>/', gameDispatcher, name="gameDispatcher"),
    path('', gameDispatcher, name="gameDispatcher"),
]
