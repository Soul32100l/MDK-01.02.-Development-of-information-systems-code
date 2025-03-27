from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('report/', views.report, name="report"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
from django.urls import path
from .views import home, about, register, user_login, report

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("report/", report, name="report"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
]