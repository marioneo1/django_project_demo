from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django import forms
from django.views.decorators.csrf import csrf_exempt

MIN_PRICE = 0
MAX_PRICE = 999999999

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})

def product_by_id(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_details.html',{'product':product})

def search(request):
    params = request.GET
    keyword = params.get('keyword','')
    min_price = params.get('min_price',MIN_PRICE)
    max_price = params.get('max_price',MAX_PRICE)
    if not isinstance(keyword, str): keyword = ""

    try:
        min_price = int(min_price)
    except ValueError:
        min_price = MIN_PRICE
       
    try:
        max_price = int(max_price)
    except ValueError:
        max_price = MAX_PRICE


    products = Product.objects.filter(name__contains=keyword,price__lte=max_price,price__gte=min_price)
    product_dict = serializers.serialize('python',products)
    actual_data = {'posts':[product['fields'] for product in product_dict]}
    return HttpResponse(f'{actual_data}')

@csrf_exempt
def add_products(request):
    # print(request.POST.get('name'))
    print(request.POST)
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f'201 Created')
        else:
            # dict(form.errors)
            return HttpResponse(f'400 Bad Request, {form.errors}')

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

