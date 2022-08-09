from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.productoView, name="Inicio"),
    path('productos', views.viewProduct, name="Productos"),
    path('chat', views.newMessage, name="Chat"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('buscar/',views.buscar, name="resultadosBusqueda"),
]
