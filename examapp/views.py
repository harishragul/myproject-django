from django.shortcuts import render
from django.http import HttpResponse
from . models import Subject, Question

# Create your views here.
def subject(request):
    subjects = Subject.objects.all()

    context = {'subjects':subjects}
    return render(request, 'examapp/subject.html', context)

def question(request, subject_id):
    id = subject_id
    questions = Question.objects.all()

    context = {'questions': questions, 'id': id}
    return render(request, 'examapp/question.html', context)
