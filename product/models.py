from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayır'))
    title = models.CharField(max_length= 100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank= True, upload_to= 'images/')
    status = models.CharField(max_length=10, choices= STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank= True, null= True, related_name= 'children', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayır'))
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    title = models.CharField(max_length= 150)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField(blank=True)
    amount = models.IntegerField(blank=True)
    detail = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(blank=True, max_length= 150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    title = models.CharField(max_length=100, blank= True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'






