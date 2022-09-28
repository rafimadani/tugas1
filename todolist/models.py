from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    title = models.CharField(max_length=50)
    description = models.TextField()
