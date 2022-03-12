from functools import cache
from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

"""   
def home(request):
    '''
    mv = cache.get('movie','has_expired')
    if mv == 'has_expired':
        cache.set('movie','idiot 1' , 20)
        mv = cache.get('movie')
    '''
    mv = cache.get_or_set('fees',5000,30)
    return render(request,'enroll/course.html',{'fm': mv})

"""


"""  
def home(request):
    data = {'name': 'Iqbal' , 'roll' : 317}
    cache.set_many(data,20)
    sv = cache.get_many(data)
    return render(request,'enroll/course.html',{'stu': sv})
"""



def home(request):
    cache.delete('roll')
    return render(request,'enroll/course.html')
