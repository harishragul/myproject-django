from django.shortcuts import render
from django.http import HttpResponse
from . models import Subject

# Create your views here.
def subjects(request):
    subjects = Subject.objects.all()

    context = {'subjects':subjects}
    return render(request, 'examapp/subject.html', context)
