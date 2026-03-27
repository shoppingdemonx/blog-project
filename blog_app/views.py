from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Post,PostImages
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    # profile = Profile.objects.get(user=request.user)
    posts = Post.objects.all()
    context = {
        # 'profile':profile,
        'posts':posts
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
            if Profile.objects.filter(user=request.user).exists():
                return redirect('home')
            else:
                return redirect('edit_profile')
        
        
    return render(request,'blog_app/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')




def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        passwd1 = request.POST.get('passwd1')
        passwd2 = request.POST.get('passwd2')
        
        if passwd1 != passwd2:
            messages.error(request,"Password doesn't match!")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists!")
            return redirect('signup')
        
        user = User.objects.create_user(username=username,email=email,password=passwd1)
        user.save()
        messages.success(request,"Account created successfully!💐")
        return redirect('login') # after edit profile page created should redirect to there
    return render(request,'blog_app/signup.html')


def edit_profile(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile_pic = request.FILES.get('profile_pic') 

        profile, created = Profile.objects.get_or_create(user=request.user)

        profile.bio = bio

        if profile_pic:
            profile.profile_pic = profile_pic

        profile.save()
        messages.success(request,"Profile Updated successfully.")
        return redirect('home')
    return render(request,'blog_app/edit_profile.html')