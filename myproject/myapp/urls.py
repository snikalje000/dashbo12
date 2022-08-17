"""myproject URL Configuration

The `urlpatterns` list routes URLs to viewsiews. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function viewsiews
    1. Add an import:  from my_app import viewsiews
    2. Add a URL to urlpatterns:  path('', viewsiews.home, name='home')
Class-based viewsiews
    1. Add an import:  from other_app.viewsiews import Home
    2. Add a URL to urlpatterns:  path('', Home.as_viewsiew(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('home',views.home),
    path('login/',views.loginPage),
    path('logout/',views.loginPage),
    path('register/',views.register),
    path('',views.landing),
    
 
    path('dashboard/',views.dashboard),
    
    
    path('dash1/',views.dash1),
    path('dash2/',views.dash2),
    path('dash3/',views.dash3),
    path('dash4/',views.dash4),
    path('dash5/',views.dash5),
    path('dash6/',views.dash6),
    path('dash7/',views.dash7),
    path('dash8/',views.dash8),
    path('dash9/',views.dash9),
    path('dash10/',views.dash10),
    path('dash11/',views.dash11),
    path('dash12/',views.dash12),
    path('dash13/',views.dash13),
    path('dash14/',views.dash14),
    path('dash15/',views.dash15),
    path('dash16/',views.dash16),
    path('dash17/',views.dash17),
    path('dash18/',views.dash18),
    path('dash19/',views.dash19),
    path('dash20/',views.dash19),
    path('dash21/',views.dash19),
 
]
