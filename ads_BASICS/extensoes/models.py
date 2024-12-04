from django.db import models

# Create your models here.

class Extensoes(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    professor = models.CharField(max_length=150, null=True, blank=True)
    assunto = models.CharField(max_length=250, null=True, blank=True)