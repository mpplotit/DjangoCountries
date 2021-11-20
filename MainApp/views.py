from django.shortcuts import render
import json
import math
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


def get_countries_list(request, page_number):
    period = 10
    countries_name_list = []
    for country_dict in countries:
        countries_name_list.append(country_dict.get('country'))
    max_page_number = math.ceil(len(countries_name_list) / period)
    countries_name_list = countries_name_list[(page_number - 1) * period:page_number * period]
    page_list = [i for i in range(1, max_page_number + 1)]
    context = {'Page': {'title': 'Список стран'},
               'Countries': countries_name_list,
               'Alfavit': Alfavit,
               'page_number': page_number,
               'max_page_number': max_page_number,
               'page_list': page_list}
    return render(request, 'countries_list.html', context)


def get_country(request, country_name):
    for country_dict in countries:
        if country_dict.get('country') == country_name:
            country = country_dict
            context = {'Page': {'title': f'Описание страны {country_name}'},
                       'Country': country
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


def get_languages_list(request):
    languages_name_list = []
    for country_dict in countries:
        languages_name_list += country_dict.get('languages')
    languages_name_list = list(set(languages_name_list))
    languages_name_list.sort()
    context = {'Page': {'title': 'Список языков мира'},
               'Languages': languages_name_list,
               'Alfavit': Alfavit}
    return render(request, 'languages_list.html', context)


def get_countries_from_language(request, language_name):
    countries_name_list = []
    for country_dict in countries:
        if language_name in country_dict.get('languages'):
            countries_name_list.append(country_dict.get('country'))
    countries_name_list = list(set(countries_name_list))
    countries_name_list.sort()
    print(countries_name_list)
    context = {'Page': {'title': f'Список стран, говорящих на языке {language_name}'},
               'Countries': countries_name_list,
               'Alfavit': Alfavit}
    return render(request, 'countries_list.html', context)
