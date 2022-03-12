from django.urls import path
from . import views

urlpatterns = [
    path('', views.findforme, name='findforme'),
    path('search/', views.search, name='search'),
    
]
