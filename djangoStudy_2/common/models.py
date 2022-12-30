from django.db import models


# Create your models here.
class Player:
    name = models.CharField(max_length=5, primary_key=True)
    pw = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.subject
