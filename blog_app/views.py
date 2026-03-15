from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'blog_app/home.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
    return render(request,'blog_app/login.html')
