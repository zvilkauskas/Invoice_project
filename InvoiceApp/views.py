from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views import generic
from .forms import UserLoginForm

from django.contrib.auth.models import User, auth



# Index view: loads registration.html instead of some kind of index page
def index(request):
    context = {}
    return render(request, 'registration/login.html', context)


# Registration view
@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'User name {username} is taken!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with this email {email} is already registered!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    messages.info(request, f'User {username} registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('register')
    return render(request, 'registration/register.html')
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         first_name = form.cleaned_data.get('first_name')
    #         last_name = form.cleaned_data.get('last_name')
    #
    #         email = form.cleaned_data.get('email')
    #         password1 = form.cleaned_data.get('password1')
    #         password2 = form.cleaned_data.get('password2')
    #         user = authenticate(
    #             username=username, first_name=first_name, last_name=last_name,
    #             email=email, password1=password1, password2=password2
    #         )
    #         login(request, user)
    #         messages.success(request, 'Jūsų paskyra buvo užregistruota!')
    #         return redirect('login')
    #     else:
    #         messages.error(request, 'Įvyko klaida, bandykite dar kartą.')
    # else:
    #     form = RegistrationForm()
    # return render(request, 'registration/register.html', {'form': form})



def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'dashboard'

    actual_decorator = user_passes_test(lambda user: user.is_anonymous, login_url=redirect_url)
    if function:
        return actual_decorator

@anonymous_required
# # Index view: loads login.html instead of some kind of index page
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
            return redirect('dashboard')
        else:
            context['form'] = form
            messages.error(request, 'Blogi prisijungimo duomenys')
            return redirect('login')
    return render(request, 'registration/login.html', context)

@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)
