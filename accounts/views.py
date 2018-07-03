from django.shortcuts import render
from .forms import UserLoginForm, UserCreationForm, ProfileRegistrationForm

# Create your views here.
def get_home(request):
    return render(request, "index.html")

def login(request):
    form = UserLoginForm()
    return render(request, "accounts/login.html", { "form": form })
    
def register(request):
    form = UserCreationForm()
    profile_form = ProfileRegistrationForm()
    return render(request, "accounts/register.html", { "form": form, "profile_form": profile_form })
    