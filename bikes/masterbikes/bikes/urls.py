from django.urls import path, include
from rest_framework import routers
from bikes import views
from .views import *


router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet)


urlpatterns = [
    path('',principal,name='principal' ),
    path('registro',registro,name='registro' ),
    path('catalogo/', catalogo, name='catalogo'),
    path('ordenarn', ordenarn, name='ordenarn'),
    path('ordenarc', ordenarc, name='ordenarc'),
    path('producto/<str:producto_nombre>/', detalle_producto_view, name='detalle_producto'),
    path('buscar', buscar, name='buscar'),
    path('vendedor', vendedor, name='vendedor'),
    path('bodeguero', vendedor, name='bodeguero'),
    path('contador', vendedor, name='contador'),
    path('carrito/', carrito, name='carrito'), 
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('api/', include(router.urls)),
    path('dolar/', dolar, name='dolar'),
]



