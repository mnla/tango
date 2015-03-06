from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("Rango says hey there world! <p> <a href='about'>about</a>")
'''


def index(request):
    context_dict = {'boldmessage' : 'I am bold font from the context'}
    return render(request, 'rango/index.html', context_dict)


'''
def about(request):
	html = "Rango says here is the about page. <p> <a href='/rango/'> index </a>"
	return HttpResponse(html)
'''

def about(request):
    return render(request, 'rango/about.html')
