from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobremi/', views.sobre_mi, name='sobremi'),
    path('contacto/', views.contacto, name='contacto'),
]