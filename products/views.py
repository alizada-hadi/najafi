from itertools import product
from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import BuyForm, SaleForm, ProductForm
from django.contrib import messages
from products.models import Buy, Product,Sale
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage
# Create your views here.

def index(request, page=1):
    q = request.GET.get("query") if  request.GET.get("query") != None else ""
    products = Product.objects.filter(
        Q(product_name_en__icontains=q) | Q(product_name_fa__icontains=q) | Q(quality__icontains=q)
    )
    # pagination
    paginator = Paginator(products, 6)
    

    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products
    } 
    return render(request, "products/product_list.html", context)

def product_create_view(request):
    if request.method =="POST":
        forms = ProductForm(request.POST, request.FILES )
        if forms.is_valid():
           forms.save()
           return redirect("product-list")
    else:
        forms = ProductForm()
    context = {
        "forms" : forms
    }
    return render(request,"products/product_form.html", context)

def product_update_view(request,pk):
    products = Product.objects.get(pk=pk)
    if request.method == 'POST':
        forms = ProductForm(request.POST, request.FILES ,nstance=products)
        if forms.is_valid():
            forms.save()
            messages.success(request,"product updated successfully")
            return redirect("product-list")
    
    else:
        forms = ProductForm(instance=products)
    context = {
        "products": products,
        "forms": forms
    } 
    return render(request,"products/product_form.html", context)


def product_delete_view(request):
    if request.method == "POST":
        id = request.POST.get("product_id")
        product = Product.objects.get(pk=id)
        product.delete()
    return redirect("product-list")

def buy_create_view(request):
    if request.method =="POST":
        forms = BuyForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Buy done successfully")
            return redirect("buy-list")
    else:
        forms = BuyForm()

    context = {
        'forms':forms }
    return render(request,'buy/buy_form.html', context)

def buy_list_view(request):
    buys = Buy.objects.all()
    context = {
        'buys': buys
    }
    return render(request, 'buy/buy_list.html', context)

def buy_update_view(request,pk):
    buys = Buy.objects.get(pk=pk)
    if request.method == "POST":
        forms = BuyForm(request.POST, instance=buys)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Buy updated successfully")
            return redirect("buy-list")
    else:
        forms = BuyForm(instance=buys)
    context ={
        "buys": buys,
        "forms": forms
    }
    return render(request, "buy/buy_form.html", context)


def buy_delete_view(request):
    if request.method == "POST":
        id = request.POST.get("buy_id")
        buy = Buy.objects.get(pk=id)
        buy.delete()
    return redirect("buy-list")


def buy_detail_view(request, pk):

    buys = Buy.objects.get(pk=pk)
    

    context = {
        
        "buys" : buys
    }

    return render(request, "buy/buy_detail.html", context)


def sale_create_view(request):
    if request.method =="POST":
        forms = SaleForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "sale created successfully")
            return redirect("sale-list")
    else:
        forms = SaleForm()
    context = {
        "forms": forms
    }   
    return render(request, "sales/sale_form.html", context)

def sale_list_view(request):
    sales = Sale.objects.all()
    context={
        "sales": sales
    }
    return render(request,"sales/sale_list.html", context)

def sale_update_view(request, pk):
    sales = Sale.objects.get(pk=pk)
    if request.method=="POST":
        forms = SaleForm(request.POST, instance=sales)
        if forms.is_valid():
            forms.save()
            messages.success(request, "sale updated succesfully")
            return redirect("sale-list")
    else:
        forms = SaleForm(instance=sales)
    context= {
        "sales": sales,
        "forms": forms
    }
    return render(request, "sales/sale_form.html",context)


def sale_delete_view(request):
    if request.method =="POST":
        id = request.POST.get("sale_id")
        sale = Sale.objects.get(pk=id)
        sale.delete()
    return redirect("sale-list")

