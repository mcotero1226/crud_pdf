"""comercializadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from categoria import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/',views.iniciar_sesion, name='login'),
    path('logout/',views.cerrar_sesion, name='logout'),
    path('categoria/',views.lista_categoria, name='lista_categoria'),
    path('categoria/agregar/',views.agregar_categoria, name='agregar_categoria'),
    path('categoria/editar/<int:id>/',views.editar_categoria, name='editar_categoria'),
    path('categoria/eliminar/<int:id>/',views.eliminar_categoria, name='eliminar_categoria'),
    path('categoria/reporte/pdf/', views.generar_reporte_pdf, name='reporte_pdf'),
    path('categoria/dashboard/', views.dashboard_productos, name='dashboard_productos'),



]