from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^log_in', views.l, name='l'),
    re_path(r'^sign_in', views.s, name='s'),
    path('logout', views.log_out, name='log_out')
]