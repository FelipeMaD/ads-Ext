# Generated by Django 5.1 on 2024-12-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(blank=True, null=True, upload_to='disciplinas/')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('professor', models.TextField(blank=True, null=True)),
            ],
        ),
    ]