from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="aboutpage"),
    path('contact/', views.contact_us, name="contactpage"),
    path('service/', views.service, name="servicepage"),
    path('menu/', views.menu, name="menupage"),
    path('advice/', views.advice, name="advicepage"),
]
