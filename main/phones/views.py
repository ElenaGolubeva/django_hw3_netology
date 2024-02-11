from django.shortcuts import render, redirect
import csv

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    list = Phone.objects.all()
    if sort_pages == 'name':
        list = Phone.objects.order_by('name')
    if sort_pages == 'min_price':
        list = Phone.objects.order_by('price')
    if sort_pages == 'max_price':
        list = Phone.objects.order_by('-price')
    context = {'phones': list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_1 = Phone.objects.get(slug=slug)
    context = {'phone': phone_1}
    return render(request, template, context)