
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('usuarios.urls')),
    path('xlsmaker/', include('xlsmaker.urls')),
    path('admin/', admin.site.urls),
     
   
]
