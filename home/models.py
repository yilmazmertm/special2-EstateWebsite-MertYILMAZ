from django.db import models

# Create your models here.

class Setting(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayır'))
    title = models.CharField(max_length= 150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank= True, max_length=150)
    phone = models.CharField(blank= True, max_length=15)
    fax = models.CharField(blank= True, max_length=15)
    email = models.CharField(blank= True, max_length=100)
    smtpserver = models.CharField(blank= True, max_length=20)
    smtpemail = models.CharField(blank= True, max_length=20)
    smtppassword = models.CharField(blank= True, max_length=20)
    smtpport = models.CharField(blank= True, max_length=10)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title