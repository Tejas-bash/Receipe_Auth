from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_logout(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        
        data = request.POST

        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user  = User.objects.filter(username = username)

        if user.exists():
            messages.success(request, "User is already there with this name")
            return redirect('/register/')
        
        user = User.objects.create(first_name=firstname, last_name=lastname, username=username)
        user.set_password(password)
        user.save()

        messages.success(request,'Your Profile has been created')
        return redirect('/register/')
    return render(request, 'register.html')

def Sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            username = data.get('username')
            password = data.get('password')

            if not User.objects.filter(username = username).exists():
                messages.error(request,'Invalid Username')
                return redirect('/login/')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request,'Invalid Password')
                return redirect('/login/')
            else:
                login(request, user)
                return HttpResponseRedirect('/Receipe/')

        else:
            return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/Receipe/')
    

@login_required(login_url = '/login/')
def receipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            receipe_image = request.FILES.get('receipe_image')
            receipe_name = data.get('receipe_name')
            receipe_description = data.get('receipe_description')
            Receipe.objects.create(receipe_image=receipe_image,receipe_name=receipe_name, receipe_description=receipe_description)

            return HttpResponseRedirect(reverse('receipes'))

        queryset = Receipe.objects.all()

        if request.GET.get('Search'):
            queryset = queryset.filter(receipe_name__icontains=request.GET.get('Search'))

        context = {'Receipe': queryset}
        return render(request, 'receipes.html', context)
    else:
        return HttpResponseRedirect('/login/')

def delete_receipe(request, id):
    if request.user.is_authenticated:
        queryset = Receipe.objects.get(id=id)
        queryset.delete()
        return HttpResponseRedirect('/Receipe/')
    else:
        return HttpResponseRedirect('/login/')


def update_receipe(request, id):

    if request.user.is_authenticated:

        queryset = Receipe.objects.get(id=id)

        if request.method == 'POST':
            data = request.POST
            receipe_image = request.FILES.get('receipe_image')
            queryset.receipe_name = data.get('receipe_name')
            queryset.receipe_description = data.get('receipe_description')

            if receipe_image:
                queryset.receipe_image = receipe_image

            queryset.save()
            return redirect('/Receipe/')

        context = {'Receipe': queryset}
        return render(request, 'update_receipe.html', context)
    else:
        return HttpResponseRedirect('/login/')
    

def Home(request):
    data = Receipe.objects.all()
    if request.GET.get('Search'):
            if request.GET.get('Search') == data:
                data = data.filter(receipe_name__icontains=request.GET.get('Search'))
    return render(request,'Home.html',{'Receipe':data})