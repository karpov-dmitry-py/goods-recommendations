"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
import app.views as app_views

router = routers.DefaultRouter()
router.register(r'categories', app_views.CategoryViewSet)
router.register(r'products', app_views.ProductViewSet)
router.register(r'properties', app_views.PropertyViewSet)
router.register(r'products_properties', app_views.ProductPropertyViewSet)
router.register(r'categories_key_properties', app_views.CategoryKeyPropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
