from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from product.models import Product


def index(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata = Product.objects.all()[:4]
    context = {'setting': setting, 'page': 'home', 'sliderdata': sliderdata}
    return render(request, 'index.html', context)

def aboutus(request):
    setting = Setting.objects.get(pk = 1)
    context = {'setting': setting, 'page' : 'aboutus'}
    return render(request, 'aboutus.html', context)

def referances(request):
    setting = Setting.objects.get(pk = 1)
    context = {'setting': setting, 'page' : 'referances'}
    return render(request, 'referances.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Mesajınız gönderilmiştir.')
            return HttpResponseRedirect('/contact')


    setting = Setting.objects.get(pk = 1)
    form = ContactFormu()
    context = {'setting': setting, 'form' : form}
    return render(request, 'contact.html', context)