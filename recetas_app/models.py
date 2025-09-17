from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField(help_text="Lista de ingredientes (uno por línea o separada por comas)")
    tiempo_minutos = models.PositiveIntegerField(verbose_name="Tiempo (minutos)")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="recetas")

    def __str__(self):
        return self.nombre
