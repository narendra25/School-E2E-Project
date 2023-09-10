from django.urls import path
from AuthenticationApp import views                     #Import the Authentication Views
urlpatterns = [
    path('',views.Login_View,name='login'),              #Login Page Url
    path('signup/',views.SignUp_View,name='signup'),     #SignUp page Url
    path('logout/',views.LogOut,name="logout")
]