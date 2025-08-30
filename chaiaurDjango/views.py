from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse(request,"hello world, welcome to Home page")
    return render(request,'websites/index.html')


def contact(request):
    return render(request,'websites/contact.html')

def about(request):
    return render(request,'websites/about.html')

def portfolio(request):
    return render(request,"websites/portfolio.html")