from django.shortcuts import render
from django.http import HttpResponse
from .forms import PrDeForm
from .forms import BrDeForm
#from . import extractor
from . import extractorclone
import pandas as pd

#from django.views.generic import TemplateView

# Create your views here.
#@ensure_csrf_cookie
#class HomeView(TemplateView):

"""def index(request):
    #return HttpResponse('Welcome to Twitter Sentiment')
    return render(request, 'LSVC/index.html', {
        'title':'Hello from index.html! Select product for review analysis here.'
    })
"""
def home(request):
    return render(request, 'LSVC/home.html')  

def products(request):
    #if request.method == 'POST':
    form = PrDeForm(request.POST)
    if form.is_valid() and form.cleaned_data():
        form.save()
        brand = form.cleaned_data['brand']
        prod = form.cleaned_data['product']
        modelname1 = form.cleaned_data['modelname1']
        modelname2 = form.cleaned_data['modelname2']
        modelname3 = form.cleaned_data['modelname3']
        modelname4 = form.cleaned_data['modelname4']
    pform = PrDeForm()
    return render(request, 'LSVC/products.html', {'form': form})

def brands(request):
    #if request.method == 'POST':
    form = BrDeForm(request.POST)
    if form.is_valid() and form.cleaned_data():
        form.save()
        prod = form.cleaned_data['product']
        brand1 = form.cleaned_data['brand1']
        brand2 = form.cleaned_data['brand2']
        brand3 = form.cleaned_data['brand3']
        brand4 = form.cleaned_data['brand4']
    bform = BrDeForm()
    return render(request, 'LSVC/brands.html', {'form': form})

def productanalyze(request):
    product_brand_form = PrDeForm(request.POST or None)
    print('View - ProductAnalyze',product_brand_form.is_valid(), sep='        ')
    if request.POST and product_brand_form.is_valid():
        brand_is = product_brand_form.cleaned_data['brand']
        product_is = product_brand_form.cleaned_data['product']

        model_is1 = product_brand_form.cleaned_data['modelname1']
        print (brand_is, product_is, model_is1, sep='      ')
        data1 = extractorclone.primary(brand_is, product_is, model_is1, 'pie1')

        model_is2 = product_brand_form.cleaned_data['modelname2']
        print (brand_is, product_is, model_is2, sep='      ')
        data2 = extractorclone.primary(brand_is, product_is, model_is2,'pie2')
        count = 2

        model_is3 = product_brand_form.cleaned_data['modelname3']
        if model_is3:
            print (brand_is, product_is, model_is3, sep='      ')
            data3 = extractorclone.primary(brand_is, product_is, model_is3,'pie3')
            count = 3
        else:
            data3 = 0;

        model_is4 = product_brand_form.cleaned_data['modelname4']
        if model_is4:
            print (brand_is, product_is, model_is4, sep='      ')
            data4 = extractorclone.primary(brand_is, product_is, model_is4,'pie4')
            count = 4
        else:
            data4 = 0;

        dic = {data1:model_is1, data2:model_is2, data3:model_is3, data4: model_is4}
        data = max(data1,data2,data3,data4)
        data = dic.get(data)
        data = data[:1].upper() + data[1:]

        print(type(model_is3))
        print(type(model_is4))
        print(bool(model_is3))
        print(bool(model_is4))
        compared = 'model'

        return render(request, "LSVC/analyze.html", {'data': data, 'count': count, 'compared': compared})
    return render(request, "LSVC/products.html", {'data': product_brand_form})

def brandanalyze(request):
    brand_form = BrDeForm(request.POST or None)
    print('View - BrandAnalyze',brand_form.is_valid(), sep='        ')
    print(brand_form.errors)
    if request.POST and brand_form.is_valid():
        product_is = brand_form.cleaned_data['product']

        brand_is1 = brand_form.cleaned_data['brand1']
        print (product_is, brand_is1, sep='      ')
        data1 = extractorclone.primary(product_is, brand_is1,'', 'pie1')

        brand_is2 = brand_form.cleaned_data['brand2']
        print (product_is, brand_is2, sep='      ')
        data2 = extractorclone.primary(product_is, brand_is2,'', 'pie2')
        count = 2

        brand_is3 = brand_form.cleaned_data['brand3']
        if brand_is3:
            print (product_is, brand_is3, sep='      ')
            data3 = extractorclone.primary(product_is, brand_is3,'', 'pie3')
            count = 3
        else:
            data3 = 0;

        brand_is4 = brand_form.cleaned_data['brand4']
        if brand_is4:
            print (product_is, brand_is4, sep='      ')
            data4 = extractorclone.primary(product_is, brand_is4,'', 'pie4')
            count = 4
        else:
            data4 = 0;

        dic = {data1:brand_is1, data2:brand_is2, data3:brand_is3, data4: brand_is4}
        data = max(data1,data2,data3,data4)
        data = dic.get(data)
        data = data[:1].upper() + data[1:]

        print(type(brand_is3))
        print(type(brand_is4))
        print(bool(brand_is3))
        print(bool(brand_is4))
        compared = 'brand'

        return render(request, "LSVC/analyze.html", {'data': data, 'count': count, 'compared': compared})
    else:
        print('Else')
        messages.error(request, "Error")
    return render(request, "LSVC/error.html", {'form': BrDeForm()})
    #return render(request, "LSVC/analyze.html", {'data': data})



