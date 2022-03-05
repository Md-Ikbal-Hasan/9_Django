from pipes import Template
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView , ListView, DetailView

from first_app  import models


# function view
""" 
def index_test(request):
    return HttpResponse("Hello World .Function view") 
"""



#class view
""" 
class IndexView(View):
    def get(self , request):
        return HttpResponse("Hello World. Class View")
"""

"""   
class IndexView(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # kw = keyword , args = arguments . Its dictionary.....
        context['sample_text_1'] = "sample text 11111111"
        context['sample_text_2'] = "sample text 22222222"
        return context
"""

"""    
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'
"""

