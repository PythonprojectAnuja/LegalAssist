from django.urls import path  # path of urls import from main project folder
from . import views  # same folder views and urls
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import include

urlpatterns = [
    path('', views.home, name="home"),
    path('contactus/', views.contactus),
    path('Service/', views.service),
    path('location/', views.location, name="loc"),
    path('signup/', views.registrationform, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
    path('visitors/', views.visit),
    path('all/', views.all),
    path('filter/', views.filter),
    path('exclude/', views.exclude),
    path('order_by/', views.order_by),
    path('create/', views.create),
    path('delete/', views.delete),
    path('update/', views.update)

]