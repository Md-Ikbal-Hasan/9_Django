from django.shortcuts import render
from Login_app.forms import * # importing all forms from Login_app
from Login_app.models import UserInfo
from django.contrib.auth.models import User


from django.contrib.auth import authenticate ,login  ,logout  # for authenticated login and logout......
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def login_page(request):
    return render(request , 'Login_app/login.html' ,context={})


def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username , password =password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_app:index')) 

            else:
                return HttpResponse("Account is not active!!")

        else:
            return HttpResponse("Login details are wrong")

    else:
        HttpResponseRedirect(reverse('Login_app:login'))




@login_required       # if user is not logged in he can't see logout option......
def user_logout(request):     
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:index'))




def index(request):
    dict = {}
    if request.user.is_authenticated:  # if user is logged in
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        dict = {'user_basic_info' : user_basic_info, 'user_more_info' : user_more_info}


    
    return render(request , 'Login_app/index.html'  ,context= dict)


def register(request):
    registered = False
     
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()          # user_form ar data gulo save kore abar saved datagulo user object a rekheci
            user.set_password(user.password) # user object a password field ar password tike encrypt koreci
            user.save()                      # then setike abar save koreci. avabe password encrypted hoyeche

            
            # user_info_form a thaka data gulo save kore user_info object a rekheci.but commit = False ar karone database a data save hobe na
            user_info = user_info_form.save(commit=False) 
            user_info.user = user     # ai line tar kaj ki???????????

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            

            user_info.save()

            registered = True


    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()


    dict = {'user_form' : user_form   , 'user_info_form' : user_info_form  ,  'registered' : registered}
    return render(request , 'Login_app/register.html' , context=dict)

