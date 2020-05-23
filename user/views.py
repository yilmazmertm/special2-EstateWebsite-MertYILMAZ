from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from product.models import Category, Product
from home.views import login_view
from user.forms import UserUpdateForm, ProfileUpdateForm


def user_index(request):
    category = Category.objects.all()
    if request.user.is_anonymous is not True:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'category': category, 'profile': profile}
        return render(request, 'user_profile.html', context)
    else:
        return HttpResponse(login_view(request))


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been Updated!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password is updated')
            return redirect('change_password')
        else:
            messages.error(request, 'Please Correct the error. <br>' + str(form.errors))
            return redirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
            'category': category
        }
        return render(request, 'change_password.html', context)


def list_estate_waiting(request):
    return render(request, 'user_estate_waiting.html')


def list_estate(request):
    category = Category.objects.all()
    current_user = request.user
    products = Product.objects.filter(user_id=current_user.id, status='True')
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'user_estate.html', context)

def list_estate_waiting(request):
    category = Category.objects.all()
    current_user = request.user
    products = Product.objects.filter(user_id=current_user.id, status='False')
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'user_estate_waiting.html', context)
