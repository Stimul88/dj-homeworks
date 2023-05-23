from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_for_pagi = []
        for row in reader:
            dict_for_pagi  = {'Name': row['Name'], 'Street':row['Street'], 'District': row['District']}
            list_for_pagi.append(dict_for_pagi)
        list_for_pagi.pop(0)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(list_for_pagi, 10)
        page = paginator.get_page(page_number)

        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
