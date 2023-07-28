"""Recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from App.views import *
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Receipe/', views.receipe, name='receipes'),
    path('delete_receipe/<id>/', views.delete_receipe, name='delete_Receipe'),
    path('update-receipe/<id>', views.update_receipe, name='update_receipe'),
    path('register/',views.register,name = 'register'),
    path('login/',views.Sign_in,name = 'Sign_in'),
    path('Userlogout/',views.user_logout,name='Userlogout'),
    path('',views.Home,name='Home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
