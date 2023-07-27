from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.http import HttpResponse


def receipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        Receipe.objects.create(receipe_image=receipe_image,
                               receipe_name=receipe_name, receipe_description=receipe_description)
        return redirect('/')

    queryset = Receipe.objects.all()

    if request.GET.get('Search'):
        queryset = queryset.filter(
            receipe_name__icontains=request.GET.get('Search'))

    context = {'Receipe': queryset}
    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        queryset.receipe_name = data.get('receipe_name')
        queryset.receipe_description = data.get('receipe_description')

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context = {'Receipe': queryset}
    return render(request, 'update_receipe.html', context)
