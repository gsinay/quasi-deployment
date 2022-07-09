from django.shortcuts import render
from . import models, forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "base_app/index.html")

def register(request): 
    registered = False
    if request.method == "POST":  #CHECKING IF USER HAS SUBMITTED FORM
        user_form = forms.UserForm(request.POST) #ASSIGNING ANSWER TO VARIABLES
        profile_form = forms.UserInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save() #CREATING USER

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm() #IF USER HASN'T YET COMPLETED FORM, JUST SHOW THE HTML
        profile_form = forms.UserInfoForm()

    return render(request, "base_app/register.html", {"user_form" : user_form, "profile_form" : profile_form, "registered" : registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("AACOUNT NOT ACTIVE. PLEASE SIGN UP")
        else:
            print("Someone tried to log in and failed")
            print("Username: {} Password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'base_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required()
def wall(request):
    return render(request, 'base_app/wall.html')

def trauma(request):
    if request.method == "POST":
        clave = request.POST.get("Clave")
        if clave.lower() == "marsexo":
            return render(request, 'base_app/buen_trauma.html', {})
        else:
            return render(request, 'base_app/mal_trauma.html', {})
    else:
        return render(request, 'base_app/pre_trauma.html', {})

def feedback_form(request):
    if request.method == "POST":
        form = forms.FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "base_app/thanks.html")
    else:
        form = forms.FeedbackForm()
        return render(request, "base_app/feedback.html", {"form" : form})
def youto(request):
    return render(request, "base_app/Pre_youto", {})




    