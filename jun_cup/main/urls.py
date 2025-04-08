from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_detect/', views.sign_detect, name='sign_detect'),
    path('registration/', views.registration, name='registration'),
]