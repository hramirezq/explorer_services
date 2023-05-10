"""
URL configuration for explorer_services_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from explorer_services_api.type_of_service.presentation.views.type_of_service_view import TypeOfServiceViewSets

router = DefaultRouter()
router.register(r'services', TypeOfServiceViewSets, basename='services')

urlpatterns = router.urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path("services/", TypeOfServiceViewSets.as_view({'get': 'list'}), name="services"),
#     path("services/", TypeOfServiceViewSets.as_view({'get': 'list'}), name="services"),
#     path("services/<int:pk>/", TypeOfServiceViewSets.as_view({'get': 'retrieve'}), name="service-detail"),
# ]

