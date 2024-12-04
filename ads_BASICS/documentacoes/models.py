from django.db import models

# Create your models here.

class Documentacoes(models.Model):
    arquivo = models.FileField(upload_to='documentacoes/', null=True, blank=True)