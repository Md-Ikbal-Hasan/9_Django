from django.shortcuts import render
from django.views.generic.base import TemplateView , RedirectView



# Create your views here.
class IkbalRedirectView(RedirectView):
    url = 'https://md-ikbal-hasan.github.io/portfolio/'
    

class ShaonRedirectView(RedirectView):
    #url = '/'
    pattern_name =  'ikbal' # se khuje ber korbe kon path ar name ikbal. sei path k call korbe
    

class BijoyRiderectView(RedirectView):
    pattern_name = 'mindex'
    permanent = True
    query_string =  True

    def get_redirect_url(self,*args,**kwargs):
        print(kwargs)
        return super().get_redirect_url(*args,**kwargs)