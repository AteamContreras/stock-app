from django.urls import path
from . import views
import requests

urlpatterns = [
    path('aboutpage/', views.about, name="aboutpage"),
    path('', views.home, name="homepage"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('delete/<stock_id>', views.delete, name="delete"),

]