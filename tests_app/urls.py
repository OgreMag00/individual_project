from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='tests_index'),
    path('<int:test_num>/', views.test, name='test_1_page'),
]
