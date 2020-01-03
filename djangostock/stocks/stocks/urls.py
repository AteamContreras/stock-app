from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #This is our homepage 
    path('', include('quotes.urls')),
]
