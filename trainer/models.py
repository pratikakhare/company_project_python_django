from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    

