"""UniversityManagement URL Configuration

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
from ast import pattern
from re import Pattern
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
# from jazzmin.urls import jazzmin_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('mainApp.urls')),
    
    path('i18n/', include('django.conf.urls.i18n')),
    
    # path('', include("admin.site.urls")),
    path('apis/', include('Scolarité.urls')),
    path('media/', include('mediaLoader.urls')),
    # path('jazzmin/', jazzmin_urls),
    path('', admin.site.urls),
]
