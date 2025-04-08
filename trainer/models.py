from django.db import models

class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subjects = models.ManyToManyField(Subject, related_name='trainers')

    def __str__(self):
        return self.name
