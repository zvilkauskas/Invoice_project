from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from .models import Client, Product, Service, Invoice, CompanyInfo
from .forms import AddNewClientForm, AddNewProductForm, AddNewServiceForm, CreateNewInvoiceForm, \
    EditInvoiceForm, EditProductForm, EditServiceForm, EditClientForm, EditCompanyInfoForm, AddCompanyInfoForm, \
    UserUpdateForm, ProfileUpdateForm

from django.urls import resolve
from django.shortcuts import render
import json


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


# --------------------- INDEX, MAIN PAGE, COMPANY INFO, CLIENTS, PRODUCTS, SERVICES, INVOICES VIEWS --------------------
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


@login_required
def company_info(request):
    company = CompanyInfo.objects.get(company_id=1)
    context = {
        'current_route': resolve(request.path_info).url_name,
        'company': company,
        'title': 'Įmonės rekvizitai'
    }
    return render(request, 'main_page.html', context)


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
    invoices = Invoice.objects.all().order_by('-invoice_number')
    context = {
        'invoices': invoices,
        'current_route': resolve(request.path_info).url_name,
        'title': 'Sąskaitos'
    }
    return render(request, 'main_page.html', context)


# -------------------------------- CREATE COMPANY INFO, CLIENT, PRODUCT, SERVICE VIEWS ---------------------------------
@login_required
def add_company_info(request):
    if request.method == 'POST':
        form = AddCompanyInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Įmonės rekvizitai išsaugoti')
            return redirect('company_info')
        else:
            messages.error(request, 'Nepavyko')
            return redirect('add_company_info')
    else:
        form = AddCompanyInfoForm()
        context = {
            'current_route': resolve(request.path_info).url_name,
            'title': 'Įmonės rekvizitai',
            'form': form
        }
    return render(request, 'main_page.html', context)


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


# Function view to add_create product.
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


# Function view to add_create service.
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
        # gauname rezultata is JS
        json_of_products_services = request.POST.get('invoice_products_services')
        # cia vyksta serializacija
        list_of_p_s = json.loads(json_of_products_services)
        # sukuriamas naujas stringas, kuriame graziai israsoma saskaitos informacija
        pretty_string = ""
        for element in list_of_p_s:
            pretty_string += f"Prekė: {element['name']}, Kiekis: {element['quantity']}vnt., " \
                             f"Kaina: {element['price']}€, Suma: {element['total']}€\n"

        invoice_form = CreateNewInvoiceForm(request.POST)
        # sukurtas forms.py metodas set_invoice_products_services, kuris leidzia django pakeisti duomenis
        invoice_form.set_invoice_products_services(pretty_string)
        if invoice_form.is_valid():
            invoice_form.save()
            messages.success(request, 'Sąskaita išsaugota')
            return redirect('invoices')
        else:
            messages.error(request, 'Nepavyko')
            return redirect('create_invoice')

    invoice_form = CreateNewInvoiceForm()
    all_products = Product.objects.all()
    all_services = Service.objects.all()

    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Nauja sąskaita',
        'invoice_form': invoice_form,
        'all_products': all_products,
        'all_services': all_services,
    }
    return render(request, 'main_page.html', context)


# ------------------------------- EDIT COMPANY, INVOICE, PRODUCT, SERVICE, CLIENT VIEWS --------------------------------
@login_required
def edit_company_info(request, pk):
    company_object = CompanyInfo.objects.get(company_id=pk)
    if request.method == 'POST':
        form = EditCompanyInfoForm(data=request.POST, instance=company_object)
        if form.is_valid():
            change_form = form.save(False)
            change_form.save()
            return redirect('company_info')
    else:
        form = EditCompanyInfoForm(instance=company_object)
    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Įmonės rekvizitų redagavimas',
        'form': form,
        'company_object': company_object
    }
    return render(request, 'main_page.html', context)


@login_required
def edit_invoice(request, pk):
    invoice = Invoice.objects.get(invoice_id=pk)
    if request.method == 'POST':
        form = EditInvoiceForm(data=request.POST, instance=invoice)
        if form.is_valid():
            change_form = form.save(False)
            change_form.save()
            return redirect('invoices')
    else:
        form = EditInvoiceForm(instance=invoice)
    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Sąskaitos redagavimas',
        'form': form
    }
    return render(request, 'main_page.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.get(product_id=pk)
    if request.method == 'POST':
        form = EditProductForm(data=request.POST, instance=product)
        if form.is_valid():
            change_form = form.save(False)
            change_form.save()
            return redirect('products')
    else:
        form = EditProductForm(instance=product)
    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Produkto redagavimas',
        'form': form
    }
    return render(request, 'main_page.html', context)


@login_required
def edit_service(request, pk):
    service = Service.objects.get(service_id=pk)
    if request.method == 'POST':
        form = EditServiceForm(data=request.POST, instance=service)
        if form.is_valid():
            change_form = form.save(False)
            change_form.save()
            return redirect('services')
    else:
        form = EditServiceForm(instance=service)
    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Paslaugos redagavimas',
        'form': form
    }
    return render(request, 'main_page.html', context)


@login_required
def edit_client(request, pk):
    client = Client.objects.get(client_id=pk)
    if request.method == 'POST':
        form = EditClientForm(data=request.POST, instance=client)
        if form.is_valid():
            change_form = form.save(False)
            change_form.save()
            return redirect('clients')
    else:
        form = EditClientForm(instance=client)
    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Kliento redagavimas',
        'form': form
    }
    return render(request, 'main_page.html', context)


# ----------------------------------- DELETE INVOICE, PRODUCT, SERVICE, CLIENT VIEWS -----------------------------------
@login_required
def delete_invoice(request, pk):
    invoice = Invoice.objects.get(invoice_id=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoices')

    context = {
        'current_route': resolve(request.path_info).url_name,
    }
    return render(request, 'main_page.html', context)


@login_required
def delete_product(request, pk):
    product = Product.objects.get(product_id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {
        'current_route': resolve(request.path_info).url_name,
    }
    return render(request, 'main_page.html', context)


@login_required
def delete_service(request, pk):
    service = Service.objects.get(service_id=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('services')

    context = {
        'current_route': resolve(request.path_info).url_name,
    }
    return render(request, 'main_page.html', context)


@login_required
def delete_client(request, pk):
    client = Client.objects.get(client_id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')

    context = {
        'current_route': resolve(request.path_info).url_name,
    }
    return render(request, 'main_page.html', context)


# --------------------------------------------- INVOICE HTML TEMPLATE VIEW ---------------------------------------------
@login_required
def invoice_template(request, pk):
    invoice_html_template = Invoice.objects.get(invoice_id=pk)
    company_details = CompanyInfo.objects.get(company_id=1)
    splitted_data = invoice_html_template.invoice_products_services.split('\n')
    print(splitted_data)
    context = {
        'invoice_html_template': invoice_html_template,
        'company': company_details,
        'splitted_data': splitted_data
    }
    return render(request, 'invoice_template.html', context)


# ------------------------------------------------- USER PROFILE VIEW --------------------------------------------------
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profilis atnaujintas')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'current_route': resolve(request.path_info).url_name,
        'title': 'Vartotojo profilis',
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'main_page.html', context)
