from django.urls import path
from . import views

urlpatterns = [
    path('', views.hiragana, name='startpage'),
    path('hiragana/', views.hiragana, name='hiragana'),
    path('<character>/', views.quiz_character, name='quiz_character'),
    path('<character>/<submission>', views.check_answer, name='check_answer'),
]
