"""wage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views
from master.views import doctor_list, DoctorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view),
    path('login/', views.LoginView.as_view()),
    path('login/refresh/', views.AccessRefreshView.as_view(), name='login_refresh'),
    path('list/', doctor_list),
    path('doctor_details/', DoctorListView.as_view()),

]
