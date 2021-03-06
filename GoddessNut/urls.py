"""GoddessNut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blog.views import index, productos, estilo, contacto, accesorios, registrar, listado_productos, nuevo_producto
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('productos/', productos, name='productos'),
    path('estilo/', estilo, name='estilo'),
    path('contacto/', contacto, name='contacto'),
    path('accesorios/', accesorios, name='accesorios'),
    path('registrar/', registrar, name='registrar'),
    path('listado-productos/', listado_productos, name='listado_productos'),
    path('nuevo-producto/', nuevo_producto, name= 'nuevo_producto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
