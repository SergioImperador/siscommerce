# coding=utf-8


from django.urls import path

from catalog.views import product_list, category, product

app_name = 'catalog'

urlpatterns = [
	path('', product_list, name='product_list'),
	path('<slug>/', category, name='category'),
	path('produtos/<slug>/', product, name='product'),
]