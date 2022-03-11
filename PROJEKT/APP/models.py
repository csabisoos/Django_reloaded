from django.db import models

# Create your models here.



class Kerdes(models.Model):
    class Meta:
        verbose_name = 'Kérdés'
        verbose_name_plural = 'Kérdések'
    
    kerdes = models.CharField(max_length=255)
    helyesvalasz = models.CharField(max_length=255)
    rosszvalasz1 = models.CharField(max_length=255)
    rosszvalasz2 = models.CharField(max_length=255)
    rosszvalasz3 = models.CharField(max_length=255)
    szam = models.IntegerField()
    logikai = models.BooleanField()
    valosszam = models.FloatField()
    hosszuszoveg = models.TextField()
    email = models.EmailField()
    url = models.URLField()

    def __str__(self): #ToString ekvivalense pythonban
        return f"{self.kerdes}: {self.helyesvalasz}"