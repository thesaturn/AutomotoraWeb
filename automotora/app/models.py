from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    númeropuertas = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=200)
    fechapublicación = models.DateTimeField()
    precio = models.PositiveIntegerField()

    def publish(self):
        self.publised_date= timezone.now()
        self.save

    def __str__(self):
        return self.title
