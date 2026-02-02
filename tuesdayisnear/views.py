#from django.http import HttpResponse (sends plain text (or raw HTML) back to the browser)
from django.shortcuts import render #use an HTML page and fill it with data

def homepage(request):
    # return HttpResponse("Hi bitch!!!, let's fuck")
    return render(request, "home.html")

def aboutpage(request):
    # return HttpResponse("This is about our affairs")
    return render(request, "about.html")
