from django import forms
from .models import Receta, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]
        labels = {"nombre": "Nombre de la categoría"}

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ["nombre", "ingredientes", "tiempo_minutos", "categoria"]
        labels = {
            "nombre": "Nombre",
            "ingredientes": "Ingredientes",
            "tiempo_minutos": "Tiempo (minutos)",
            "categoria": "Categoría",
        }

    def clean_tiempo_minutos(self):
        t = self.cleaned_data.get("tiempo_minutos")
        if t is None or t <= 0:
            raise forms.ValidationError("El tiempo debe ser un número positivo.")
        return t
