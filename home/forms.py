from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from product.models import Product, Images


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    catid = forms.IntegerField()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='User Name')
    email = forms.EmailField(max_length=200, label='Email')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='Fist Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class AddEstateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'keywords', 'description','image', 'price', 'm2', 'room_number', 'age_of_building',
                  'city', 'detail')

class AddEstateImages(ModelForm):
    class Meta:
        model = Images
        fields = ('title', 'image')
