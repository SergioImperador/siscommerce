# coding=utf-8

from django.urls import path

from accounts.views import register, index, update_user, update_password

app_name = 'accounts'


urlpatterns = [
    path('', index, name='index'),
    path('alterar-dados/', update_user, name='update_user'),
    path('alterar-senha/', update_password, name='update_password'),
    path('registro/', register, name='register'),
]
