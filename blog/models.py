from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.CharField (max_length=100)
    cantidad = models.IntegerField()

class Pedidos(models.Model):
    idPedidos = models.IntegerField(primary_key=True)
    fechaCompra = models.DateField()
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class DetallePedido (models.Model):
    idDetallePedido = models.IntegerField(primary_key=True)
    precio = models.IntegerField()
    descuento = models.IntegerField()

class Cliente (models.Model):
    idCliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    cuidad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    codigoPostal = models.IntegerField()
    numeroTelefono = models.IntegerField()
