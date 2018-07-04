from .views import login, register, logout, profile
from django.urls import path


urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),
    path('profile/', profile, name="profile"),
    ]