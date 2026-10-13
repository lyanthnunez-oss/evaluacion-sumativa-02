from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    fundacion = models.IntegerField()
    presupuesto = models.IntegerField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.IntegerField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
