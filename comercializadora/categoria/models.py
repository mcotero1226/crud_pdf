from django.db import models  # Importa el módulo de modelos de Django

# Modelo Producto
class categoria(models.Model):  # Define una clase llamada Producto que hereda de models.Model
    idcategoria = models.CharField(max_length=100)  # Campo de texto para el nombre del producto, máximo 100 caracteres
    nombre = models.CharField(max_length=100)  # Campo de texto largo para la descripción del producto
    descripcion = models.CharField(max_length=10) 
    estado= models.CharField(max_length=100)  # Campo de texto para el nombre del producto, máximo 100 caracteres
    

    def __str__(self):  # Método especial para representar el objeto como una cadena
        return self.nombre  # Devuelve el nombre del producto como representación en texto

# Create your models here.
