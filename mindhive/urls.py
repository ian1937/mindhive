"""mindhive URL Configuration

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
from roster.views import role_views, shift_views, employee_views, availability_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('roles/', role_views.roles, name='roles'),
    path('roles/<id>', role_views.role, name='role'),
    path('shifts/', shift_views.shifts, name='shifts'),
    path('shifts/<id>', shift_views.shift, name='shift'),
    path('employees/', employee_views.employees, name='employees'),
    path('employees/<id>', employee_views.employee, name='employee'),
    path('availabilities/', availability_views.availabilities, name='availabilities'),
    path('availabilities/<id>', availability_views.availability, name='availability'),
]
