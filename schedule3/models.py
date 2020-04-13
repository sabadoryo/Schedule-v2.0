from django.db import models


# Create your models here.

class Subjects(models.Model):
    title = models.CharField(max_length=200)


class Groups(models.Model):
    title = models.CharField(max_length=6)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)