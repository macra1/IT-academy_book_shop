from django.shortcuts import render
from django.http import HttpResponse
from .airports_id import read_and_filter

# Create your views here.


def main_wd(request):
    return render(request, "main_wd.html", context={})


def airport_main(request):
    answer = {"first_10": ['AAA', 'AAB', 'AAC', 'AAE', 'AAF', 'AAG', 'AAH', 'AAI', 'AAJ', 'AAK']}
    return render(request, template_name="base.html", context=answer)


def what_id(request, id_airport):
    answer = {"id_airport": id_airport.upper(), "answer": read_and_filter(id_airport)}
    return render(request, template_name="index.html", context=answer)

