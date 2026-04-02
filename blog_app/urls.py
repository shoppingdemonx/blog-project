from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('become-creator/',views.become_creator,name='become_creator'),
    path('send-otp/',views.send_otp,name='send-otp'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
]