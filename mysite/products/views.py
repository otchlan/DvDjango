from django.shortcuts import render

from .models import Product, SuperProduct
from django.http import HttpResponseRedirect

#from .forms import nameForm

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

def get_title(request):
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/products/')
    else:
        form = productForm()

    return render(request, "product_detail.html", {'form': form})