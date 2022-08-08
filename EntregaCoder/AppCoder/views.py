# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import productoFormulario

def productoView(request):
    return render(request, 'AppCoder/index.html')

def viewProduct(request):
    """
    Vista de las personas de la familia

    Obtiene todos los objetos de la base de datos del modelo AppFamilia
    Retorna plantilla en HTML para visualizar los datos en forma de formulario
    """
    producto = productos.objects.all()
    lista_nombre = []

    for product in producto:
        lista_nombre.append({"title":product.title,
                             "price":product.price,
                             "thumbnail":product.thumbnail})

    return render(request, "AppCoder/productos.html",{"context":lista_nombre})

def cursoFormulario(request):
    if request.method == "POST":
        productForm = productoFormulario(request.POST)
        print(productForm)
        if productForm.is_valid:
            informacion = productForm.cleaned_data
            product = productos( title=informacion['title'], price=informacion['price'], thumbnail=informacion['thumbnail'])
            product.save()
            producto = productos.objects.all()
            lista_nombre = []
            for product in producto:
                lista_nombre.append({"title":product.title,
                                    "price":product.price,
                                    "thumbnail":product.thumbnail})
            return render(request, "AppCoder/productos.html",{"context":lista_nombre})
    else:
        productForm = productoFormulario()
    return render(request,"AppCoder/cursoFormulario.html", {"productForm":productForm})