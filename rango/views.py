from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <p> <a href='about'>about</a>")
    
def about(request):
	html = "Rango says here is the about page. <p> <a href='/rango/'> index </a>"
	return HttpResponse(html)
