from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from . forms import ContactForm

def home(request):
  products = Product.objects.all()[:8]
  context = {'products':products}
  return render(request, 'home/index.html', context)

def products(request):
  products = Product.objects.all()
  offer = Offer.objects.all()[:1]
  context = {'products':products}
  return render(request, 'home/products.html', context)

def productDetails(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  products = Product.objects.all()[:4]
  context = {'products':products, 'product': product}
  return render(request, 'home/product_details.html', context)

def about(request):
  return render(request, 'home/about.html')

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact  # Assuming Contact is defined in your models

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            new_contact.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})

