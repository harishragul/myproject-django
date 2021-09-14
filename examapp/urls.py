from django.urls import path
from . import views

urlpatterns = [
    path('subject', views.subject, name = 'subject')
]
