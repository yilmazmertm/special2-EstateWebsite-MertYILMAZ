from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('home/', include('home.urls')),
    path('contact/', views.contact, name = 'contact'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('referances/', views.referances, name = 'referances'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_products, name = 'category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name = 'product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

