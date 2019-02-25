"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include										 
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static

#from catalog import views as views_catalog
#from accounts import views as views_accounts
#from checkout import views as views_checkout
from django.contrib.auth import views as auth_views

from core import views					  


urlpatterns = [
	path('', views.index, name='index'),
	path('contato/', views.contact, name='contact'),
	path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('conta/', include('accounts.urls', namespace='accounts')),
	path('compras/', include('checkout.urls', namespace='checkout')),
    path('paypal/', include('paypal.standard.ipn.urls')),																  
    path('admin/', admin.site.urls),
]
