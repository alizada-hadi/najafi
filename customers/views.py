
from django.shortcuts import redirect, render

from products.models import Buy
from .forms import CustomerForm, FarmerForm
from django.contrib import messages
from .models import Customer, Farmer
from django.forms import inlineformset_factory
# Create your views here.

FarmerFormSet = inlineformset_factory(
    Farmer, Buy, fields=("name", "buyer", "quantity", "unite", "address", "date", "price", "paid_amount", "description",), extra=1, can_delete=False
)


def customer_create_view(request):
    if request.method == "POST":
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "customer created successfully")
            return redirect("customer-list")
    else:
        forms = CustomerForm()
    context ={
        'forms': forms
    }
    return render(request, 'customers/customer_form.html', context)

def customer_list_view(request):
    customers = Customer.objects.all()
    context ={
        'customers': customers
    }
    return render(request, 'customers/customer_list.html', context)

def customer_update_view(request, pk):
    customers = Customer.objects.get(pk=pk)
    if request.method == "POST":
        forms = CustomerForm(request.POST, instance=customers)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Customer updated successfully")
            return redirect("customer-list")
    else:
        forms = CustomerForm(instance=customers)
    context={
        "customers": customers,
        "forms": forms
    }
    return render(request, "customers/customer_form.html", context)
    

def customer_delete_view(request):
    if request.method == 'POST':
        id = request.POST.get("customer-id")
        
        customer = Customer.objects.get(pk = id)
        customer.delete()
    return redirect("customer-list")

def customer_detail_view(request, pk):
    customers1 = Customer.objects.get(pk=pk)
    sales = customers1.sale_set.all()
    total_sale = sales.count()
    total = 0
    paid = 0
    remain = 0
    customers = Customer.objects.all()
    for i in customers1.sale_set.all():
        total = i.total_price 
        paid = i.recieved_amount
        remain = i.remained_amount
    context ={
        "total_sale": total_sale,
        "total": total,
        "paid": paid,
        "remain": remain,
    }
    return render(request, "customers/customer_detail.html" )


def farmer_list_view(request):
    farmers = Farmer.objects.all()

    context = {
        "farmers" : farmers
    }
    return render(request, "customers/farmers/farmer_list.html", context)

def farmer_create_view(request):
    if request.method == "POST":


        forms = FarmerForm(request.POST)
        if forms.is_valid():
            farmer = forms.save()
            return redirect("farmer-detail", farmer.pk)
    else:
        forms = FarmerForm()

    context = {
        "forms" : forms
    }
    return render(request, "customers/farmers/farmer_form.html", context)

def farmer_update_view(request,pk):
    farmers = Farmer.objects.get(pk=pk)
    if request.method =="POST":
        forms = FarmerForm(request.POST, instance=farmers)
        if forms.is_valid():
            forms.save()
            return redirect("farmer-list")
    else:
        forms = FarmerForm(instance=farmers)
    return render(request,"customers/farmers/farmer_form.hmtl")
    
def farmer_detail_view(request, pk):
    
    farmers = Farmer.objects.get(pk=pk)
    buys = farmers.buy_set.all()
    total_buy = buys.count()
    total = 0
    paid = 0
    remain = 0
    if request.method == "POST":
        formset = FarmerFormSet(request.POST, instance=farmers)
        if formset.is_valid():
            formset.save()
            return redirect("farmer-list")
    else:
        formset = FarmerFormSet(instance=farmers)

    for i in farmers.buy_set.all():
        total = i.total_amount
        paid = i.paid_amount
        remain = i.remined_amount

    context = {
        'total_buy': total_buy,
        "formset" : formset,
        "farmers" : farmers, 
        "buys" : buys, 
        "total" : total, 
        "paid" : paid, 
        "remain" : remain
    }
    return render(request, "customers/farmers/farmer_detail.html", context)

def farmer_delete_view(request):
    if request.method =="POST":
        id = request.POST.get("farmer-id")
        farmer = Farmer.objects.get(pk=id)
        farmer.delete()
    return redirect("farmer-list")
