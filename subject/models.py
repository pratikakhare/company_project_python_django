from django.db import models

# Create your models here.
class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    