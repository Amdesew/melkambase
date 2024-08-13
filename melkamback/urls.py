"""
URL configuration for melkamback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from melkamapp.views import logein, home, natural_form, spare_form, OrderViewSet, samplesViewSet, CarSpareViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'samples', samplesViewSet)
router.register(r'carspare', CarSpareViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', logein),
    path('home/', home),
    path('natural_form/', natural_form),
    path('spare_form/', spare_form),
    path('api/', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
