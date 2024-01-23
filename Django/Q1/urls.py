from django.urls import path
from .views import server_info

urlpatterns = [
    path('', server_info, name='server_info'),
    # other URL patterns...
]
