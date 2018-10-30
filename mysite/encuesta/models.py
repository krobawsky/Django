from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('date published')

class Opcion(models.Model):
    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)