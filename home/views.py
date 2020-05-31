import json
import random

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from home.forms import SearchForm, SignUpForm, AddEstateForm, AddEstateImages
from home.models import Setting, ContactFormMessage, ContactFormu, FAQ, UserProfile
from product.models import Product, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    products = Product.objects.all()
    sliderdata = Product.objects.filter(status= True)
    dayproducts = Product.objects.all()[:3]
    lastproducts = Product.objects.all().order_by('-id')[:3]
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'products': products,
               'sliderdata': sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'category': category, 'setting': setting, 'page': 'aboutus'}
    return render(request, 'aboutus.html', context)


def referances(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'category': category, 'setting': setting, 'page': 'referances'}
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
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'category': category, 'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products, 'category': category, 'categorydata': categorydata, 'setting': setting}
    return render(request, 'products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    product = Product.objects.get(pk=id)
    profile = UserProfile.objects.get(user_id=product.user)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'category': category, 'product': product,
               'images': images, 'comments': comments, 'profile':profile, 'setting': setting}
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)

            context = {'products': products, 'category': category}
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/')


def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def blank_page(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'blank.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Login Hatası !")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'setting': setting}
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'form': form, 'setting': setting}
    return render(request, 'signup.html', context)

def get_random():
    return int(1000*random.random())

@login_required(login_url = '/login')
def add(request):
    ImageFormSet = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = AddEstateForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            current_user = request.user
            data = Product()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.price = form.cleaned_data['price']
            data.image = form.cleaned_data['image']
            data.m2 = form.cleaned_data['m2']
            data.room_number = form.cleaned_data['room_number']
            data.age_of_building = form.cleaned_data['age_of_building']
            data.city = form.cleaned_data['city']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.slug = str(data.category_id) + str(get_random()) + str(get_random())
            data.save()
            for f in formset:
                try:
                    photo = Images()
                    photo.product_id = data.id
                    photo.image = f.cleaned_data['image']
                    photo.title = str(data.category_id) + str(data.title) + str(get_random())
                    photo.save()
                except Exception as e:
                    break
            messages.success(request, 'Your content is inserted')
            return HttpResponseRedirect('/add')
        else:
            messages.success(request, 'Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = AddEstateForm
        formset = ImageFormSet(queryset=Images.objects.none())
        context = {
            'category': category,
            'form': form,
            'formset': formset,
            'setting': setting
        }
        return render(request, 'add.html', context)

@login_required(login_url = '/login')
def edit(request, id):
    product = Product.objects.get(id=id)
    ImageFormSet = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        form = AddEstateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            for f in formset:
                try:
                    photo = Images()
                    photo.title = str(get_random()) + str(get_random()) + str(get_random())
                    photo.save()
                except Exception as e:
                    break
            messages.success(request, 'Your Content is updated')
            return HttpResponseRedirect('/user/list_estate')
        else:
            messages.success(request, 'Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/edit/' + str(id))
    else:
        formset = ImageFormSet(queryset=Images.objects.none())
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = AddEstateForm(instance=product)
        context = {
            'category': category,
            'form': form,
            'formset':formset,
            'setting':setting
        }
        return render(request, 'add.html', context)

@login_required(login_url = '/login')
def delete(request, id):
    current_user = request.user
    Product.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Satılık ev ilanı kaldırıldı')
    return HttpResponseRedirect('/user/list_estate')


def faq(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {
        'category':category,
        'faq':faq,
        'setting':setting
    }
    return render(request, 'faq.html', context)

def allestates(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    products = Product.objects.filter(status= True)
    context = {
        'category': category,
        'products':products,
        'setting':setting
    }
    return render(request, 'allestates.html', context)
