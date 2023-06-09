from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views import generic
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from .models import Client, Product, Service, Invoice
from .forms import AddNewClientForm, AddNewProductForm, AddNewServiceForm, CreateNewInvoiceForm, SelectProductForm
from django.urls import resolve
from django.shortcuts import render
from uuid import uuid4


# ----------------------------------------- LOGIN, LOGOUT, REGISTRATION VIEWS ------------------------------------------
# register view
@csrf_protect
def register(request):
    if request.method == 'POST':
        # getting values from register form
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # position = request.POST['position']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if the passwords match
        if password == password2:
            # check if username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            # check if email exists
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                # If those ifs passes, new user ir created
                else:
                    User.objects.create_user(
                        username=username, first_name=first_name, last_name=last_name,
                        email=email, password=password
                    )
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa! Bandykite dar kartą.')
            return redirect('register')
    return render(request, 'registration/register.html')


def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'main_page'

    actual_decorator = user_passes_test(lambda user: user.is_anonymous, login_url=redirect_url)
    if function:
        return actual_decorator


@anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'registration/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main_page')
        else:
            context['form'] = form
            messages.error(request, 'Blogi prisijungimo duomenys')
            return redirect('login')
    return render(request, 'registration/login.html', context)


def logged_out(request):
    logout(request)
    return render(request, 'logged_out.html')


def search(request):
    pass


# --------------------------------- INDEX, CLIENTS, PRODUCTS, SERVICES, INVOICES VIEWS ---------------------------------

def index(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def main_page(request):
    current_route = resolve(request.path_info).url_name
    title = 'Pagrindinis'

    context = {
        'current_route': current_route,
        'title': title,
    }

    return render(request, 'main_page.html', context)


# Displays list of clients.
@login_required
def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
        'current_route': resolve(request.path_info).url_name,
        'title': 'Klientai',
    }
    return render(request, 'main_page.html', context)


@login_required
def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'current_route': resolve(request.path_info).url_name,
        'title': 'Prekės',
    }
    return render(request, 'main_page.html', context)


@login_required
def services(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'current_route': resolve(request.path_info).url_name,
        'title': 'Paslaugos',
    }
    return render(request, 'main_page.html', context)


@login_required
def invoices(request):
    invoices = Invoice.objects.all()
    context = {
        'invoices': invoices,
        'current_route': resolve(request.path_info).url_name,
        'title': 'Sąskaitos'
    }
    return render(request, 'main_page.html', context)


# --------------------------------------- CREATE CLIENT, PRODUCT, SERVICE VIEWS ---------------------------------------
# Function view to add client.
@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddNewClientForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Klientas pridėtas')
            return redirect('clients')
        else:
            messages.error(request, 'Nepavyko')
            return redirect('add_client')
    else:
        form = AddNewClientForm()
        context = {
            'current_route': resolve(request.path_info).url_name,
            'title': 'Klientai',
            'form': form
        }
    return render(request, 'main_page.html', context)


# Function view to add product.
@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddNewProductForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Prekė pridėta')
            return redirect('products')
        else:
            messages.error(request, 'Nepavyko')
            return redirect('add_product')
    else:
        form = AddNewProductForm()
        context = {
            'current_route': resolve(request.path_info).url_name,
            'title': 'Prekės',
            'form': form
        }
    return render(request, 'main_page.html', context)


# Function view to add service.
@login_required
def add_service(request):
    if request.method == 'POST':
        form = AddNewServiceForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Paslauga pridėta')
            return redirect('services')
        else:
            messages.error(request, 'Nepavyko')
            return redirect('add_service')
    else:
        form = AddNewServiceForm()
        context = {
            'current_route': resolve(request.path_info).url_name,
            'title': 'Paslaugos',
            'form': form
        }
    return render(request, 'main_page.html', context)

@login_required
def create_full_invoice(request):
    if request.method == 'POST':
        invoice_form = CreateNewInvoiceForm(request.POST)
        if invoice_form.is_valid:
            invoice_form.save()
            messages.success(request, 'Sąskaita išsaugota')
            return redirect('invoices')
        else:
            messages.error(request, 'Nepavyko')
            return redirect('create_invoice')

    invoice_form = CreateNewInvoiceForm()
    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Nauja sąskaita',
        'invoice_form': invoice_form,
    }
    return render(request, 'main_page.html', context)

