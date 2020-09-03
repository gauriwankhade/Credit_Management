"""Credit_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from creditapp.views import homeView,userlistView,transferView,userView,profileView,transactionView,credithistoryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='home'),
    path('users',userlistView,name='users_list'),
    path('transfer',transferView,name='transfer_url'),
    path('add',userView,name='add_user'),
    path('transfer/profile/<pk>/',profileView,name='profile_url'),
    path('transaction/<pk>/',transactionView,name='transaction_url'),
    path('credithistory',credithistoryView,name='history_url'),


]