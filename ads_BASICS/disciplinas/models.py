from django.db import models

# Create your models here.

class Disciplinas(models.Model):
    imagem = models.FileField(upload_to='disciplinas/', blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    professor = models.TextField(blank=True, null=True)
    