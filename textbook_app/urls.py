from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='textbook_index'),
    path('<int:textbook_p>', views.textbook, name='textbook_page')
]
