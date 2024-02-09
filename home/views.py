from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext

from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def error_400(request, exception):
    data = {}
    return render(request,'400.html', data)

def error_403(request, exception):
    data = {}
    return render(request,'403.html', data)

def error_404(request, exception):
    data = {}
    return render(request,'404.html', data)

def error_500(request, *args, **argv):
    return render(request,'500.html', status=500)