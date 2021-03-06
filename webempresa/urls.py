"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from core import views

"""
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba)

"""

urlpatterns = [

    #Para el core
    path('', include('core.urls')),

    #Para la administración
    path('admin/', admin.site.urls),
]

#Para poder servir ficheros media en de la bbdd
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
