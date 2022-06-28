from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView
# Create your views here.

class HomeTemplateViw(TemplateView):
    template_name= 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {
        #     'name' : "sunny",
        #     'roll' : 1020
        # }
        
        context['name'] = "ikbal"
        context['roll'] = 10101

        print(kwargs)
        return context