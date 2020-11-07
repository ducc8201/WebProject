from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def home(request):
    Allproducts = Product.objects.all()
    paginator = Paginator(Allproducts,1)
    pagenum = request.GET.get('page',1)
    numPage = paginator.num_pages ### get numer of page
    print()
    try:
        products = paginator.page(pagenum)
    except (EmptyPage,InvalidPage,ValueError):
        products = paginator.page(1)

    context = {
        'products' : products,
        'numPage' : range(1,numPage+1),

    }
    return render(request,'store/home.html',context)