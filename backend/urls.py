from django.http import JsonResponse
from django.urls import path

def hello(request):
    return JsonResponse({"message": "Hello DevOps with Django"})

urlpatterns = [
    path('', hello),
]
