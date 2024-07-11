from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required #automatically checks if the user is logged in 
def home(request):
        return render(request, "home.html", {"form":form}) 


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()  # Initialize the form for GET requests

    return render(request, "registration/signup.html", {"form": form})