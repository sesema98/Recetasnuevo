from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Receta, Categoria
from .forms import RecetaForm, CategoriaForm

def receta_list(request):
    q = request.GET.get("q", "").strip()
    recetas = Receta.objects.select_related("categoria").all()
    if q:
        recetas = recetas.filter(
            Q(nombre__icontains=q) |
            Q(ingredientes__icontains=q) |
            Q(categoria__nombre__icontains=q)
        )
    return render(request, "recetas_app/receta_list.html", {"recetas": recetas, "q": q})

def receta_create(request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recetas_app:receta_list")
    else:
        form = RecetaForm()
    return render(request, "recetas_app/receta_form.html", {"form": form, "accion": "Crear Receta"})

def receta_update(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect("recetas_app:receta_list")
    else:
        form = RecetaForm(instance=receta)
    return render(request, "recetas_app/receta_form.html", {"form": form, "accion": "Editar Receta"})

def receta_delete(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        receta.delete()
        return redirect("recetas_app:receta_list")
    return render(request, "recetas_app/receta_confirm_delete.html", {"receta": receta})

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, "recetas_app/categoria_list.html", {"categorias": categorias})

def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recetas_app:categoria_list")
    else:
        form = CategoriaForm()
    return render(request, "recetas_app/categoria_form.html", {"form": form, "accion": "Crear Categoría"})

def categoria_update(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect("recetas_app:categoria_list")
    else:
        form = CategoriaForm(instance=cat)
    return render(request, "recetas_app/categoria_form.html", {"form": form, "accion": "Editar Categoría"})

def categoria_delete(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        cat.delete()
        return redirect("recetas_app:categoria_list")
    return render(request, "recetas_app/categoria_confirm_delete.html", {"obj": cat})

def categoria_detail(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    recetas = cat.recetas.all()
    return render(request, "recetas_app/categoria_list.html", {"categorias": [cat], "detalle": True, "recetas": recetas})
