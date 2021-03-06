# -*- coding: utf-8 -*- 
"""fact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^terceros/$",'aplic.views.terceros'),
    url(r"^kardex/$",'aplic.views.kardex'),
    url(r'^kardex/crear/$','aplic.views.Crear_kardex'),
    url(r'^terceros/crear/$','aplic.views.Crear_tercero'),
    url(r"^usuarios/$",'aplic.views.usuarios'),
    url(r'^usuarios/crear/$','aplic.views.Crear_usuario'),
    url(r"^productos/$",'aplic.views.productos'),
    url(r'^productos/crear/$','aplic.views.Crear_producto'),
    url(r'^usuarios/editar/(?P<id>\d+)/$','aplic.views.prueba'),
    url(r'^parametro/crear/$','aplic.views.Crear_parametro'),
    url(r'^$','aplic.views.index',name='incio'),
    url(r'^login/$','auten.views.login_view',name='vista_login'),
    url(r'^logout/$','auten.views.logout_view',name='vista_logout')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

