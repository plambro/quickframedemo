from django.shortcuts import render, redirect

from .models import CleanData
from .utils import clean_data, dataset


def index(request):
    datalist = CleanData.objects.all()
    context = {'datalist': datalist}
    return render(request, 'index.html', context)


def clean(request):
    clean_data(dataset)
    return redirect('index')
