from django.db import models

# Create your models here.
class Projetos(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField()
    parceria = models.CharField(max_length=200, null=True, blank=True)
    conclusao = models.DateField()
    tecnologias = models.TextField()