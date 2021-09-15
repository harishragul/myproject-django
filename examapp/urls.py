from django.urls import path
from . import views

urlpatterns = [
    path('subject', views.subjects, name = 'subject')
]
