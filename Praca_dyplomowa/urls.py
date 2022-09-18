"""Praca_dyplomowa URL Configuration

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
from strona import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', views.IndexView.as_view(), name='index_view'),
    path('services/', views.ServiceView.as_view(), name='service_list_view'),
    path('service/<int:pk>/', views.DetailServiceView.as_view(), name='detail_service_view'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('service_add/', views.ServiceAddView.as_view(), name='service_add_view'),
    path('service_delete/<int:pk>/', views.ServiceDeleteView.as_view(), name='service_delete_view'),
    path('service_update/<int:pk>/', views.ServiceUpdateView.as_view(), name='service_update_view'),
    path('rooms/', views.RoomView.as_view(), name='room_list_view'),
    path('room/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail_view'),
    path('room_add/', views.RoomAddView.as_view(), name='room_add_view'),
    path('room_delete/<int:pk>/', views.RoomDeleteView.as_view(), name='room_delete_view'),
    path('smarts/', views.SmartView.as_view(), name='smart_list_view'),
    path('smart/<int:pk>/', views.SmartDetailView.as_view(), name='smart_detail_view'),
    path('smart_add/', views.SmartAddView.as_view(), name='smart_add_view'),
    path('smart_delete/<int:pk>/', views.SmartDeleteView.as_view(), name='smart_delete_view'),
    path('typeofspots/', views.TypeOfSpotView.as_view(), name='typeofspot_list_view'),
    path('typeofspot/<int:pk>/', views.TypeOfSpotDetailView.as_view(), name='typeofspot_detail_view'),
    path('typeofspot_add/', views.TypeOfSpotAddView.as_view(), name='typeofspot_add_view'),
    path('typeofspot_delete/<int:pk>/', views.TypeOfSpotDeleteView.as_view(), name='typeofspot_delete_view'),
    path('spots/', views.SpotView.as_view(), name='spot_list_view'),
    path('spot/<int:pk>/', views.SpotDetailView.as_view(), name='spot_detail_view'),
    path('spot_add/', views.SpotAddView.as_view(), name='spot_add_view'),
    path('spot_delete/<int:pk>/', views.SpotDeleteView.as_view(), name='spot_delete_view'),
    path('room_update/<int:pk>/', views.RoomUpdateView.as_view(), name='room_update_view'),
    path('smart_update/<int:pk>/', views.SmartUpdateView.as_view(), name='smart_update_view'),
    path('typeofspot_update/<int:pk>/', views.TypeOfSpotUpdateView.as_view(), name='typeofspot_update_view'),
    path('spot_update/<int:pk>/', views.SpotUpdateView.as_view(), name='spot_update_view'),
]
