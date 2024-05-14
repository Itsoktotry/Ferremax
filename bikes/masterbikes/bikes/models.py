from django.db import models
from django.utils import timezone





class Categoria(models.Model):
    nombrecat = models.CharField(max_length=100, primary_key=True)  # Cambiando el campo nombre a clave primaria
    
    def __str__(self):
        return self.nombrecat
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.TextField(default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, to_field='nombrecat')  # Estableciendo la relación con to_field='nombre'
    precio = models.DecimalField(max_digits=10, decimal_places=2 , default=0.00)


    def __str__(self):
        return self.nombre

class Stock(models.Model):
    cantidad = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def str(self):
        return f"Stock de {self.producto.nombre}: {self.cantidad}"






