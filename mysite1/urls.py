from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('contact/', views.contact, name = 'contact'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('referances/', views.referances, name = 'referances'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_products, name = 'category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name = 'product_detail'),
    path('search/', views.product_search, name = 'product_search'),
    path('search_auto/', views.product_search_auto, name = 'product_search_auto'),
    path('logout/', views.logout_view, name = 'logout_view'),
    path('login/', views.login_view, name = 'login_view'),
    path('blank/', views.blank_page, name = 'blank_page'),
    path('signup/', views.signup_view, name = 'signup_view'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

