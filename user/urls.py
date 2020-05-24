from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('list_estate/', views.list_estate, name='list_estate'),
    path('list_estate_waiting/', views.list_estate_waiting, name='list_estate_waiting'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),


]
