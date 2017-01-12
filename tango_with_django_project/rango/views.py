from django.http import HttpResponse
from django.shortcuts import render
import getpass


context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!", 'username': getpass.getuser()}


def index(request):
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context=context_dict)
