from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/<int:id>/results', views.results_quiz, name='results'),
    path('quiz/<int:id>/', views.quiz, name='quiz'),
    path('quizCreationForm', views.quizCreationForm, name='quizCreationForm'),
]
