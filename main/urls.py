from django.urls import path

from main.views import *

app_name = 'main'
urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('<str:lang>.<str:puzzleName>/', gameDispatcher, name="gameDispatcher"),
    path('<str:puzzleName>/', gameDispatcher, name="gameDispatcher"),
]
