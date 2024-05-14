from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

from .forms import ProductoForm
from bikes.Carrito import Carrito
from bikes.models import Producto
from rest_framework import viewsets
from .serializer import StockSerializer
from .models import Stock
import requests
import json

#main indexpy
def principal(request):
    productos = Producto.objects.all()
    if request.user.is_authenticated:

        return(render(request,'index.html', {'productos': productos}))
    else:
        return render(request,'index.html', {'productos': productos})
    

#registro de usuarios
def registro(request):  
    data = { 

        'form' :  CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="principal")
        data['form'] = formulario

    return render(request,'registration/registro.html',data)

#manejo de catalogo

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})



def ordenarn(request):
    productos = Producto.objects.order_by('nombre')
    return render(request, 'catalogo.html', {'productos': productos})

def ordenarc(request):
    productos = Producto.objects.order_by('categoria')
    return render(request, 'catalogo.html', {'productos': productos})




def detalle_producto_view(request, producto_nombre):
    producto = get_object_or_404(Producto, nombre=producto_nombre)
    context = {
        'producto': producto
    }
    return render(request, 'detalle_producto.html', context)





def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')  # Obtener los términos de búsqueda ingresados por el usuario
          # Obtener el tipo ingresado por el usuario
        # Filtrar los formularios que contengan el término de búsqueda en el nombre y el tipo
        formularios = Producto.objects.filter(nombre__icontains=query)

        return render(request, 'buscar.html', {'formularios': formularios, 'query': query})

def carrito(request):
    return render(request, 'carrito.html')


#vistas
def vendedor(request):
    productos = Producto.objects.all()
    return render(request, 'vendedor.html', {'productos': productos})


def bodeguero(request):
    productos = Producto.objects.all()
    return render(request, 'bodeguero.html', {'productos': productos})

def contador(request):
    productos = Producto.objects.all()
    return render(request, 'contador.html', {'productos': productos})

def detalle_producto(request):
    productos = Producto.objects.all()
    return render(request, "detalle_producto.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return render(request, 'carrito.html', {'producto_id': producto_id})


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


def dolar(request):
    url = "https://mindicador.cl/api/dolar/2024"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        valor_dolar = data["serie"][0]["valor"]
        return render(request, 'dolar.html', {'valor_dolar': valor_dolar})