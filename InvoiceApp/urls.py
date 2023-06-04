from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('main_page/', views.main_page, name='main_page'),
]