"""
URL configuration for individual_project project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'), name='main_app'),
    path('textbook/', include('textbook_app.urls'), name='textbook_app'),
    path('tests/', include('tests_app.urls'), name='tests_app'),
    path('auth/', include('auth_app.urls'), name='auth_app'),
    path('profile/', include('profile_app.urls'), name='profile_app')

]
