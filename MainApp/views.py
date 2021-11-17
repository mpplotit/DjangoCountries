from django.shortcuts import render
import json
from django.http import Http404

with open('country-by-languages.json', 'r') as jsonfile:
    content = jsonfile.read()
    countries = json.loads(content)

Alfavit = []
for i in range(65, 91):
    Alfavit.append(chr(i))


# Create your views here.
def home(request):
    context = {'Page': {'title': 'Главная страница'}}
    return render(request, 'index.html', context)


def get_countries_list(request):
    countries_name_list = []
    for country_dict in countries:
        countries_name_list.append(country_dict.get('country'))
    context = {'Page': {'title': 'Список стран'},
               'Countries': countries_name_list,
               'Alfavit': Alfavit}
    return render(request, 'countries_list.html', context)


def get_country(request, country_name):
    for country_dict in countries:
        if country_dict.get('country') == country_name:
            country = country_dict
            context = {'Page': {'title': f'Описание страны {country_name}'},
                       'Country': country,
                       }
            return render(request, 'country.html', context)
    raise Http404


def get_countries_from_letter(request, first_letter):
    if first_letter not in Alfavit:
        raise Http404
    countries_name_list = []
    for country_dict in countries:
        if country_dict.get('country')[0] == first_letter:
            print(country_dict.get('country'))
            countries_name_list.append(country_dict.get('country'))
    context = {'Page': {'title': f'Список стран на букву {first_letter}'},
               'Countries': countries_name_list,
               'Alfavit': Alfavit,
               'first_letter': first_letter}
    return render(request, 'countries_from_letter.html', context)
