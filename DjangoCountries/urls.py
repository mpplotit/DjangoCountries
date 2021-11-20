"""DjangoCountries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/page/<int:page_number>', views.get_countries_list, name='countries-list'),
    path('country/<str:country_name>', views.get_country, name='country'),
    path('countries-that-start-with-<str:first_letter>', views.get_countries_from_letter, name='countries-from-letter'),
    path('languages-list', views.get_languages_list, name='languages-list'),
    path('countries-with-language-<str:language_name>', views.get_countries_from_language,
         name='countries-from-language'),

]
