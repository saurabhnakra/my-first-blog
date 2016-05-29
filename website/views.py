from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
#class IndexView(generic.ListView):
 #   template_name = 'website/index.html'
def IndexView(request):
    return render(request, 'website/index.html', {})

def AboutView(request):
    return render(request, 'website/about.html', {})

def ContactView(request):
    return render(request, 'website/contact.html', {})