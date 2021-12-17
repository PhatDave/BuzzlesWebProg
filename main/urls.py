from django.urls import path

from main.views import *

app_name = 'main'
urlpatterns = [
    path('userPage/<str:username>/', userPage, name="userPage"),
    path('login/', siteLogin, name="login"),
    path('logout/', siteLogout, name="logout"),
    path('loginSubmit/', loginSubmit, name="loginSubmit"),

    path('register/', register, name="register"),
    path('registerSubmit/', registerSubmit, name="registerSubmit"),

    path('switchLang/<str:lang>/', switchLang, name="switchLang"),
    path('switchDiff/<int:diff>/', switchDiff, name="switchDiff"),
    path('getNewPuzzle/', getNewPuzzle, name="getNewPuzzle"),
    path('submitSolution/', submitSolution, name="submitSolution"),

    path('<str:puzzleName>/', gameDispatcher, name="gameDispatcher"),
]
