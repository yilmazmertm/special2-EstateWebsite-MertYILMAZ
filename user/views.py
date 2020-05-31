from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile, Setting
from product.models import Category, Product, Comment
from home.views import login_view
from user.forms import UserUpdateForm, ProfileUpdateForm


def user_index(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    if request.user.is_anonymous is not True:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'category': category, 'profile': profile, 'setting': setting}
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
            messages.success(request, 'Profiliniz başarı ile güncellenmiştir.')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        setting = Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'setting':setting
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarı ile değiştirilmiştir.')
            return redirect('change_password')
        else:
            messages.error(request, 'Lütfen hatayı düzeltiniz. <br>' + str(form.errors))
            return redirect('/user/password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
            'category': category,
            'setting': setting
        }
        return render(request, 'change_password.html', context)


def list_estate(request):
    category = Category.objects.all()
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    products = Product.objects.filter(user_id=current_user.id, status='True')
    context = {
        'category': category,
        'products': products,
        'setting': setting
    }
    return render(request, 'user_estate.html', context)


def list_estate_waiting(request):
    category = Category.objects.all()
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    products = Product.objects.filter(user_id=current_user.id, status='False')
    context = {
        'category': category,
        'products': products,
        'setting': setting
    }
    return render(request, 'user_estate_waiting.html', context)


def comments(request):
    category = Category.objects.all()
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    comments = Comment.objects.filter(user_id=current_user.id, status='True')
    context = {
        'category': category,
        'comments': comments,
        'setting': setting
    }
    return render(request, 'user_comments.html', context)


def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorumunuz başarı ile silindi.')
    return HttpResponseRedirect('/user/comments')
