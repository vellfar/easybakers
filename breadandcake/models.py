from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=15, null=True)
    location = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Offer(models.Model):
    price= models.CharField(max_length=200, null=True)
    title= models.CharField(max_length=200, null=True)
    description= models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Testimonial(models.Model):
    message= models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    name= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name