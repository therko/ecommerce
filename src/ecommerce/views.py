from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    context = {
        "title":"Hello world",
        "content":"Welcome to the HomePage!!",
        "premium_content":"jeah"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "jeah"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"about page",
        "content":"Welcome to the about"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"contact",
        "content":"Welcome to the contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST) 
    #     print(request.POST.get('full_name')) 
    return render(request, "contact/view.html", context)

def login_page(request):

    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)

        if user is not None:
            login(request, user)
            return redirect("/login")
        else:
            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(username, email, password)
        print(User)
    return render(request, "auth/register.html", context)        