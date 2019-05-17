from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": 'This is about me',
        "my_number": 123,
        "my_list" : [123,234,345,456,567,678,789],
    }
    return render(request, "contact.html", my_context)

def test_view(request, *args, **kwargs):
    return render(request, "test.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def index_view(request, *args, **kwargs):
    numbers = [1,2,3,4]
    name = 'Rafal Szuwaski'

    a = {'myName': name, 'numbers' : numbers}

    return render(request, "index.html",a)

def main_view(request, *args, **kwargs):
    return render(request,"main.html")

def product_detail_view(request, *args, **kwargs):
    return render(request,"/products")

