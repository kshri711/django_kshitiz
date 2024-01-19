from django.shortcuts import render
from login_app.forms import UserForm,UserProfileInfoForm

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'loginapp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            

            if 'profile_pic' in request.FILES:
                profile.profile_pic =  request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(profile_form.errors,user_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'loginapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not active!')

        else:
            print("Login Failed!")
            print("Username : ",username,"  Password : ",password)
            return HttpResponse("Invalid Credentials!")

    else:
        return render(request,'loginapp/login.html',{})

        

                

