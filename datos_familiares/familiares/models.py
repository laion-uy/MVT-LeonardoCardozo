from django.db import models

'''
>> Consigna: Crear una web que permite ver los datos de algunos de tus familiares, guardados en un BD.

Deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)
La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
Se deberán crear como mínimo 3 familiares
Los familiares se deben ver desde la web
'''

# Create your models here.
class Familiar(models.Model):
    relacion = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    altura_cm = models.IntegerField()