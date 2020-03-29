from django.contrib import admin
# Register your models here.
from product.models import Category, Product, Images

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 7

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','image_tag' ,'status', 'price']
    list_filter = ['status']
    inlines = [ProductImageInline]
    readonly_fields = ('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product','image_tag']
    readonly_fields = ('image_tag',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)

