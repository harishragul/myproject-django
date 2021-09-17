from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=2000)

    def __str__(self):
        return self.question
