from django.shortcuts import render
from .models import Product, SuperProduct


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    #context ={
     #   'title':obj.title,
     #   'description': obj.description
   # }

    context = {
        'object': obj
    }
    return render(request, "product_detail.html", context)

def super_product_detail_view(request):
    objS = SuperProduct.objects.get(id=1)

    context = {
        'sobject': objS
    }
    return render(request, "s_product_detail.html", context)