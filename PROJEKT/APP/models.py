from django.db import models

# Create your models here.


class Kerdes(models.Model):
    class Meta:
        verbose_name = 'Kérdés'
        verbose_name_plural = 'Kérdések'
    
    kerdes = models.CharField(max_length=255)
    helyesvalasz = kerdes = models.CharField(max_length=255)
    rosszvalasz1 = kerdes = models.CharField(max_length=255)
    rosszvalasz2 = kerdes = models.CharField(max_length=255)

    def __str__(self): #ToString ekvivalense pythonban
        pass
