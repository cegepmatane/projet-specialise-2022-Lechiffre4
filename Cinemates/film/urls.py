from django.urls import path
from . import views

urlpatterns = [
    path('', views.film, name='film'),
    path('<int:id>', views.film_id, name='film_id'),
    
]