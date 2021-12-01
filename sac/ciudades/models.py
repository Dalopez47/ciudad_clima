from django.db import models

class Ciudad(models.Model):

    nombre = models.CharField(max_length=255)


    def __str__(self):
        return f' {self.nombre}'




class Consulta (models.Model):

    hora = models.TimeField()
    temperatura = models.FloatField()
    humedad = models.FloatField()
    viento = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, on_delete= models.SET_NULL, null=True)


    def __str__(self):
        return f' {self.hora}: {self.temperatura} {self.humedad} {self.viento} {self.ciudad}'

