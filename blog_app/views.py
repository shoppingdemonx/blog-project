from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile':profile
    }
    return render(request,'blog_app/home.html',context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is None:
            print("Invalid Credentials!")
            return redirect('login')
        else:
            login(request,user)
            return redirect('home')
        
        
    return render(request,'blog_app/login.html')


