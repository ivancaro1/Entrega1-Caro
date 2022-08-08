from django.urls import path
from AppCoder import views

urlpatterns = [
    path('index', views.productoView, name="Inicio"),
    path('productos', views.viewProduct, name="Productos"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
]
