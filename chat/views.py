from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm
from .forms import UserForm,EditForm,Profile_form
from .models import custom 
import random
from django.core.cache import cache

a=random.randint(0,9)
b=random.randint(0,9)
# Create your views here.
def sign_up(request):
    global a,b
    sum=a+b
    try:
        if request.session['username']:
            return redirect('/user_profile/')
    except:
        if request.user.is_authenticated: 
            return redirect('/user_profile/')
        if request.method=="GET":
            form=UserCreationForm()
            return render(request,'signup.html',{"form":form,"a":a,"b":b})
        else:
            form=UserCreationForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password1']
                confirm_password=form.cleaned_data['password2']
                ans=request.POST.get('ans')
                if int(ans)!=sum:
                    print(type(ans),ans)
                    print(type(sum),sum)
                    print(sum==ans)
                    form=UserCreationForm()
                    return render(request,'signup.html',{"form":form,"a":a,"b":b})
               
                form.save()
                form=AuthenticationForm()
                return render(request,'login.html',{"form":form})
            form=UserCreationForm()
            return render(request,'signup.html',{"form":form,"a":a,"b":b})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method=="GET":
            form=AuthenticationForm()
            return render(request,'login.html',{"form":form})
        else:
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    try:
                        custom.objects.create(user=user)
                    except:
                        custom.objects.get(user=user)
                    login(request, user)
                    request.session['username']=username
                    return redirect('/user_profile/')
                else:
                    return HttpResponse("Invalid")
            else:
                return HttpResponse("Invalid")
    return redirect('/user_profile/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=EditForm(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Profile updated')
                form.save()
        else:
            form=EditForm(instance=request.user)
        return render(request,'home.html',{'name':request.user,'form':form})
    return redirect('/login/')
def user_logout(request):
    logout(request)
    return redirect('/login/')

def changepass(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user_profile/')
    form=PasswordChangeForm(user=request.user)
    return render(request,'changepass.html',{'form':form})

def details(request):
    username=request.POST.get('username')
    try:
        obj=User.objects.get(username=username)
        print(obj.pk, "id")
        ct=cache.get('count',version=obj.pk)
        if ct:
            return render(request,'details.html',{"task":obj,"val":"Online"})
        else:
            return render(request,'details.html',{"task":obj,"val":"offline"})
    except:
        msg="No such user exists"
        return render(request,'details.html',{"msg":msg})

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

def uploadPic(request,user):
    if request.method=='POST':
        form = Profile_form(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user_profile/')
    form=Profile_form()
    return render(request,'upload.html',{"form":form})



        