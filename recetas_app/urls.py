from django.urls import path
from . import views

app_name = "recetas_app"

urlpatterns = [
    # Recetas
    path("", views.receta_list, name="receta_list"),
    path("recetas/nuevo/", views.receta_create, name="receta_create"),
    path("recetas/<int:pk>/editar/", views.receta_update, name="receta_update"),
    path("recetas/<int:pk>/eliminar/", views.receta_delete, name="receta_delete"),

    # Categorías
    path("categorias/", views.categoria_list, name="categoria_list"),
    path("categorias/nuevo/", views.categoria_create, name="categoria_create"),
    path("categorias/<int:pk>/editar/", views.categoria_update, name="categoria_update"),
    path("categorias/<int:pk>/eliminar/", views.categoria_delete, name="categoria_delete"),
    path("categorias/<int:pk>/", views.categoria_detail, name="categoria_detail"),
]
