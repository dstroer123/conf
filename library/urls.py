from django.urls import path

from .views import create_author

urlpatterns = [
    path('', create_author, name='create_author')
]