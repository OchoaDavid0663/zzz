from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    foto_producto = models.ImageField(upload_to='img_productos/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_proveedor = models.IntegerField()


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Proveedor(models.Model):
    id_proveedor = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='proveedores')
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.nombre_empresa} - {self.producto.nombre}"

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
