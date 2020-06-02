from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import *
# Create your views here.

def index(request):
    context={}
    return render(request,'app/index.html',context)

def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request,'app/products.html',context)

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'app/detail.html', {'product': product})

def contact(request):
    return render(request,'app/contact.html')

def blog(request):
    return render(request,'app/blog.html')

def gallery(request):
    return render(request,'app/gallery.html')
