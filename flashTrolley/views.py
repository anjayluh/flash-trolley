from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .models import Customer, Product
from .forms import RegistrationForm, SignInForm, ProductForm
from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages


class Register(View):
    form_class = RegistrationForm
    template_name = 'flashTrolley/register.html'
    def get(self, request):
         form = self.form_class()
         return render(request, self.template_name, {'register_form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request,"You have been successfully registered, please login")
            form.save()
            return HttpResponseRedirect('/signin/')
        return render(request, self.template_name, {'register_form': form})

class AddProduct(View):
    form_class = ProductForm
    template_name = 'flashTrolleyAdmin/addproduct.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'product_form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You have successfully added a new product")
            return HttpResponseRedirect('/viewproducts/')
        return render(request, self.template_name, {'product_form': form})

class Login(View):
    form = SignInForm
    template_name = 'flashTrolley/signin.html'

    def get(self,request):
        form_method = self.form()
        return render(request, self.template_name, {'form':form_method})

    def post(self,request):
        form_method = self.form(request.POST)
        if form_method.is_valid():
            email = form_method.cleaned_data.get('email')
            customer = Customer.objects.get(email=email)
            request.session['username'] = customer.username
            return redirect('/')
        return render(request, self.template_name, {'form':form_method})

@login_required
def logout_page(request):
    logout(request)
    return redirect('/')


def view_product(request):
    # show_customer()
    context = RequestContext(request, {'request': request, 'user': request.user})
    products = Product.objects.all()
    return render(request, 'flashTrolley/index.html', {'products': products}, context_instance=context)

def admin_product(request):
    # show_all products()
    products = Product.objects.all()
    return render(request, 'flashTrolleyAdmin/viewproducts.html', {'products': products})

def view_customer(request):
    # show_all customers()
    customers = Customer.objects.all()
    return render(request, 'flashTrolleyAdmin/viewcustomers.html', {'customers': customers})


def delete_product(request,id):
   for product in Product.objects.all():
    if id == product.id:
        product.delete()
        messages.success(request, "You have successfully deleted the product")
   return render(request, 'flashTrolleyAdmin/viewproducts.html')
def edit_product(request):
   pass

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    username = request.session.get('username')  # used to check if customer is logged in
    customer = Customer.objects.get(username=username)
    if customer:
        customer.add_to_cart(product)
        return redirect(reverse('view_product'))
    else:
        return redirect(reverse('signin'))
