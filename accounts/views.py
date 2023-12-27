from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm (request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            user = authenticate(email = email, password = password1)
            login(request, user)
            return redirect("tables")
        else:
            print("Password doesn't match")
    else:
        form = UserCreationForm ()

    return render(request,"signup.html",{"form":form})




