# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *
from datetime import datetime
now = datetime.now()


def productoView(request):
    return render(request, 'AppCoder/inicio.html')

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


def newMessage(request):
    if request.method == "POST":
        newMessa = messageHub(request.POST)
        print(newMessa)
        if newMessa.is_valid():
            informacion = newMessa.cleaned_data
            mensaje = chat( user=informacion['user'], message=informacion['message'], date=now)
            mensaje.save()
            info = infoUsers( user=informacion['user'], lastmessagedate=now)
            info.save()
            mensajes = chat.objects.all()
            lista_mensajes = []
            for new in mensajes:
                lista_mensajes.append({"user":new.user,
                                    "message":new.message,
                                    "date":new.date})
            return render(request, "AppCoder/chat.html",{"context":lista_mensajes})
    else:
        newMessa = messageHub()
    message_hub = chat.objects.all()
    context = {'newMessa': newMessa, 'context': message_hub}
    return render(request,"AppCoder/chat.html", context)

def cursoFormulario(request):
    if request.method == "POST":
        productForm = productoFormulario(request.POST)
        print(productForm)
        if productForm.is_valid():
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

def buscar(request):
    producto = request.GET.get("title", None)
    print(request)
    if producto:
        print(producto)
        product = productos.objects.filter(title__icontains=producto)
        return render(request, "AppCoder/busquedaProduct.html",{"product":product})
    elif not producto:
        respuesta = "No enviaste datos"
        print(respuesta)
        return render(request,"AppCoder/busquedaProduct.html",{"respuesta":respuesta})

def viewInfoUsers(request):
    info = infoUsers.objects.all()
    lista_users = []
    for informa in info:
        lista_users.append({"user":informa.user,
                            "lastmessagedate":informa.lastmessagedate})
    return render(request, "AppCoder/infoUser.html",{"context":lista_users})