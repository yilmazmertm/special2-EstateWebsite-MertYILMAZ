from django.urls import path

from . import views

urlpatterns = [
    # ex: /product/
    path('', views.user_index, name='user_index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]
