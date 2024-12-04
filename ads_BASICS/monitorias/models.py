from django.db import models

# Create your models here.

class Monitorias(models.Model):
    imagem = models.ImageField(upload_to='monitorias/', null=True, blank=True)
    titulo = models.CharField(max_length=140, null=True, blank=True)
    descricao = models.TextField()