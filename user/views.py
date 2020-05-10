from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import UserProfile
from product.models import Category
from home.views import login_view


def user_index(request):
    category = Category.objects.all()
    if request.user.is_anonymous is not True:
        current_user = request.user
        profile = UserProfile.objects.get(user_id = current_user.id)
        context = {'category': category, 'profile': profile}
        return render(request, 'user_profile.html', context)
    else:
        return HttpResponse(login_view(request))

