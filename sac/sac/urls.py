"""sac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from ciudades.views import DatoVista, CiudadVista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datos/', DatoVista.as_view(), name='dato_lista'),
    path('datos/<int:id>', DatoVista.as_view(), name='dato_pro'),
    path('ciudades/', CiudadVista.as_view(), name='lista'),
    path('ciudades/<int:id>', CiudadVista.as_view(), name='ciudad_lista')

]
