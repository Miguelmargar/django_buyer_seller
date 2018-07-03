from .views import login, register
from django.urls import path

urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    ]