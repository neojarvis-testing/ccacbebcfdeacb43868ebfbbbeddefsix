from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('Q1.urls')),
    path('admin/', admin.site.urls),
]
