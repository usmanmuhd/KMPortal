from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    automobile_used_in = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name

class ResearchPaper(models.Model):
    title = models.CharField(max_length=1024)
    synopsis = models.TextField()
    paper = models.FileField(upload_to='research')


class Design(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    automobile_used_in = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='design')


class Requirement(models.Model):
    design = models.OneToOneField(Design, on_delete=models.CASCADE)
    requirements = models.TextField()
