

"""   
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time initialization")

    def __call__(self,request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return  response
"""


from django.http import HttpResponse


class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Brother initialization")

    def __call__(self,request):
        print("This is Brother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return  response


class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Father initialization")

    def __call__(self,request):
        print("This is Father before view")
        response = self.get_response(request)
        #response = HttpResponse("Hi")
        print("This is Father after view")
        return  response



class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Mother initialization")

    def __call__(self,request):
        print("This is Mother before view")
        response = self.get_response(request)
        print("This is Mother after view")
        return  response