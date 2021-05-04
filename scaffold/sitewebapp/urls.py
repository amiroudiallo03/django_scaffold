from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio-details.html/', views.portofolio, name="portfolio"),
    
]

