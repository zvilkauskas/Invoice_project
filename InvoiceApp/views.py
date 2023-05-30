from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views import generic
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate



# Index view: loads registration.html instead of some kind of index page
def index(request):
    context = {}
    return render(request, 'registration/login.html', context)


# Registration view
@csrf_protect
def register(request):
    # if request.method == 'POST':
        # getting values from registration form
        # username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # position = request.POST['position']
        # email = request.POST['email']
        # password = request.POST['password']
        # password2 = request.POST['password2']

        # check if the passwords match
    #     if password != password2:
    #         messages.error(request, 'Slaptažodžiai nesutampa! Bandykite dar kartą.')
    #         return redirect('register')
    #     # check if username exists
    #     if User.objects.filter(username=username).exists():
    #         messages.error(request, f'Vartotojo vardas {username} užimtas!')
    #         return redirect('register')
    #     # check if email exists
    #     if User.objects.filter(email=email).exists():
    #         messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
    #         return redirect('register')
    #     # If those ifs passes, new user ir created
    #     User.objects.create_user(
    #         username=username, first_name=first_name, last_name=last_name,
    #         position=position, email=email, password=password
    #     )
    #     messages.info(request, f'Vartotojas {username} užregistruotas!')
    #     return redirect('login')
    # return render(request, 'registration/register.html')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Jūsų paskyra buvo užregistruota!')
            return redirect('login')
        else:
            messages.error(request, 'Įvyko klaida, bandykite dar kartą.')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



def login(request):
    context = {}
    return render(request, 'registration/login.html', context)

@login_required
def dashboard(request):
    pass
