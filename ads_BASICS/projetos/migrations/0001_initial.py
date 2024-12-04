# Generated by Django 5.1 on 2024-12-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('descricao', models.TextField()),
                ('parceria', models.CharField(blank=True, max_length=200, null=True)),
                ('conclusao', models.DateField()),
                ('tecnologias', models.TextField()),
            ],
        ),
    ]
