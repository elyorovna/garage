from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import EmailForm, ContactForm
from blog.models import Joylashish, Cars, Categories


# Create your views here.
def index(request):
    cars = Cars.objects.all()
    category = Categories.objects.all()
    carousel = cars.filter(joylash=Joylashish.objects.get(name='carousel'))
    latest = cars.filter(joylash=Joylashish.objects.get(name='latest'))
    feature = cars.filter(joylash=Joylashish.objects.get(name='feature'))
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Sorov qabul qilindi<h1>")
        else:
            return HttpResponse("<h1>Sorovni toldirishda xatolik bor<h1>")
    else:
        form = EmailForm()
    context = {
        'cars': cars,
        'carousel': carousel,
        'latest': latest,
        'feature': feature,
        'form': form,
        'category': category
    }
    return render(request, 'index.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>sorov qabul qilindi<h1>")
        else:
            return HttpResponse("<h1>Sorovni toldirishda xatolik bor<h1>")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)


def detail(request, id):
    cars = Cars.objects.get(id=id)
    context = {
        'cars': cars

    }
    return render(request, 'detail.html', context=context)
def category(request, id):
    cars = Cars.objects.filter(category=Categories.objects.get(id=id))
    category = Categories.objects.all()
    carousel = cars.filter(joylash=Joylashish.objects.get(name='carousel'))
    latest = cars.filter(joylash=Joylashish.objects.get(name='latest'))
    feature = cars.filter(joylash=Joylashish.objects.get(name='feature'))
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Sorov qabul qilindi<h1>")
        else:
            return HttpResponse("<h1>Sorovni toldirishda xatolik bor<h1>")
    else:
        form = EmailForm()
    context = {
        'cars': cars,
        'carousel': carousel,
        'latest': latest,
        'feature': feature,
        'form': form,
        'category': category
    }
    return render(request, 'index.html', context=context)

