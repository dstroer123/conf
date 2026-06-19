from django.urls import path

from .views import (
    create_author,
    login_view,
    logout_view
)

urlpatterns = [
    path('', create_author, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]