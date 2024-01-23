from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
import sys
from django.conf import settings
from django.contrib.auth import views
import django

def server_info(request):
    django_version = django.get_version()
    python_version = sys.version
    debug_mode = settings.DEBUG

    response_data = {
        'django_version': django_version,
        'python_version': python_version,
        'debug_mode': debug_mode,
    }

    return JsonResponse(response_data)
