from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views import generic
from .forms import UserLoginForm
from django.contrib.auth import logout

from django.contrib.auth.models import User, auth


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
        redirect_url = 'index'

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
            return redirect('index')
        else:
            context['form'] = form
            messages.error(request, 'Blogi prisijungimo duomenys')
            return redirect('login')
    return render(request, 'registration/login.html', context)


@login_required
def index(request):
    context = {}
    return render(request, 'index.html', context)

def logged_out(request):
    logout(request)
    return render(request, 'logged_out.html')
