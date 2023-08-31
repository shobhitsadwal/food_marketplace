from django.http import HttpResponse
from django.shortcuts import render




# def home(request):
#     return HttpResponse("hello ceo of caramel coast ")


def home (request):
    return render(request,"index.html")