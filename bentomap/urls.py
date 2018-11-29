"""bentomap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.home, name = 'home'),
    path('food/', views.food, name = 'food'),
    path('index/',views.index)
<<<<<<< HEAD
=======
    path('accounts/',include('accounts.urls')),
    path('', views.home, name='home'),
>>>>>>> origin/add-accounts-app
=======
    path('accounts/',include('accounts.urls')),
>>>>>>> ac47f77013e0839cde85cf98fd96f4eb19dcdcdc
]

urlpatterns += staticfiles_urlpatterns()