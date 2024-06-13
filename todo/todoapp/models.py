from django.db import models

# Create your models here.
class Todo (models.Model):
    todotitle = models.CharField(max_length=500)
    tododescription = models.TextField()
    todostarttime = models.TimeField()
    todoendtime = models.TimeField()