"""
URL configuration for our_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name="index"),
    path('control-versiones/', views.control_versiones, name="control_versiones"),
    path('metodologias-agiles/', views.metodologias_agiles, name="metodologias_agiles"),  # ← Corregido
    path('documentacion/', views.documentacion, name="documentacion"),
    path('testing/', views.testing, name="testing"),
    path('trabajo-equipo/', views.trabajo_equipo, name="trabajo_equipo"),
    path('recursos/', views.recursos, name="recursos"),
]

