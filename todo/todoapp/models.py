from django.db import models

# Create your models here.
class Todo (models.Model):
    todotitle = models.CharField(max_length=500)
    tododesctiption = models.TextField()
    todostarttime = models.TimeField()
    todoendtime = models.TimeField()