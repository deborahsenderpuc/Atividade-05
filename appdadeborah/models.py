from django.db import models

class Musicas(models.Model):
  title = models.CharField(max_length=50)
  album = models.CharField(max_length=70)
  artista = models.CharField(max_length=70)
  release = models.DateField()

class Albums(models.Model):
  TP_ARTISTA = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('B', 'Band')
  ]
  title = models.CharField(max_length=50)
  year = models.DateField()
  musician = models.CharField(max_length=50)
  tipo = models.CharField(max_length=1,choices=TP_ARTISTA, default='')
  
