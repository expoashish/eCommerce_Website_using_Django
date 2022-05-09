from django.shortcuts import render,redirect
from ecommerce.forms import CustomerForm,CustomerAddForm,VendorForm,VendorAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from ecommerce.models import Customer,Vendor 
from django.contrib.auth.models import User


# Create your views here.
def index(request):
	return render(request,'ecommerce/index.html')

def register_page(request):
	return render(request,'ecommerce/registeras.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registerasvendor(request):
    registered=False
    if request.method=='POST':
        var_VendorForm=VendorForm(request.POST)
        var_VendorAddForm=VendorAddForm(request.POST)
        if var_VendorForm.is_valid() and var_VendorAddForm.is_valid():
            Vendorprimary=var_VendorForm.save()
            Vendorprimary.set_password(Vendorprimary.password)
            Vendorprimary.save()
            VendorAdd=var_VendorAddForm.save(commit=False)
            VendorAdd.Vendor=Vendorprimary
            VendorAdd.save()
            registered=True
    else:
        var_VendorForm=VendorForm()
        var_VendorAddForm=VendorAddForm()
    return render(request,'ecommerce/vendor_register.html',{'var_VendorForm':var_VendorForm,'var_VendorAddForm':var_VendorAddForm,'registered':registered})

def registerascustomer(request):
    registered=False
    if request.method=='POST':
        var_CustomerForm=CustomerForm(request.POST)
        var_CustomerAddForm=CustomerAddForm(request.POST)
        if var_CustomerForm.is_valid() and var_CustomerAddForm.is_valid():
            Customerprimary=var_CustomerForm.save()
            Customerprimary.set_password(Customerprimary.password)
            Customerprimary.save()
            CustomerAdd=var_CustomerAddForm.save(commit=False)
            CustomerAdd.Customer=Customerprimary
            CustomerAdd.save()
            registered=True
    else:
        var_CustomerForm=CustomerForm()
        var_CustomerAddForm=CustomerAddForm()
    return render(request,'ecommerce/customer_register.html',{'var_CustomerForm':var_CustomerForm,'var_CustomerAddForm':var_CustomerAddForm,'registered':registered})

def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('/ecommerce/loginpage/')
    else:
        return render(request,'ecommerce/loginpage.html',{'invalidlogin':invalidlogin})

@login_required
def dashboard(request):
    try:
        current=Student.objects.get(student=request.user)
    except Student.DoesNotExist:
        current=Teacher.objects.get(teacher=request.user)
    if current.is_student:
        return redirect('/customer_dash/')
    else:
        return redirect('/vendor_dash/')
    return render(request,'ecommerce/dashboard.html')

    

def customerDash(request):
    return render(request,'ecommerce/customer_dash.html')

def vendorDash(request):
    return render(request,'ecommerce/vendor_dash.html')



