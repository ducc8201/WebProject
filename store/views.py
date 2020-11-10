import json

from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import JsonResponse


# Create your views here.
def home(request):
    Allproducts = Product.objects.all()
    paginator = Paginator(Allproducts, 4)
    pagenum = request.GET.get('page', 1)
    numPage = paginator.num_pages  ### get numer of page
    print()
    try:
        products = paginator.page(pagenum)
    except (EmptyPage, InvalidPage, ValueError):
        products = paginator.page(1)

    (items,order) =Same(request)
    context = {
        'products': products,
        'numPage': range(1, numPage + 1),
        'items'  : items,
        'order'  : order,

    }
    return render(request, 'store/home.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderdetail_set.all()
    else:
        item=[]
        order={'get_total_product':0,'get_total_price_product':0}
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:', productId)
    print('action:', action)
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer)
    orderdetail,created = Orderdetail.objects.get_or_create(order=order,product = product)
    if action == 'add':
        orderdetail.quantity = (orderdetail.quantity+1)
    elif action == 'remove' :
        orderdetail.quantity = (orderdetail.quantity-1)

    return JsonResponse("cart is updated", safe=False)
def Same(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderdetail_set.all()
    else:
        item=[]
        order={'get_total_product':0,'get_total_price_product':0}

    return  (items,order);