from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete
from django.contrib.auth.models import User



@receiver(user_logged_in, sender = User)
def login_success(sender,request,user,**kwargs):
    print("----------------")
    print("Loggedin signal....Run Intro")
    print("Sender: " , sender)
    print("Request: " ,request)
    print("User Password: ", user.password)
    print(f'kwargs: {kwargs}')



@receiver(user_logged_out, sender = User)
def log_out(sender,request,user,**kwargs):
    print("----------------")
    print("Logged out signal....Run Outro..")
    print("Sender: " , sender)
    print("Request: " ,request)
    print("User Password: ", user.password)
    print(f'kwargs: {kwargs}')



@receiver(user_login_failed)
def login_failed(sender, credentials ,request,**kwargs):
    print("----------------")
    print("Login failed  signal....")
    print("Sender: " , sender)
    print("Credentials: " ,credentials)
    print("Request: " ,request)
    print(f'kwargs: {kwargs}')



@receiver(pre_save, sender = User)
def at_beginning_save(sender,instance,**kwargs):
    print("----------------")
    print("Pre Save  signal....")
    print("Sender: " , sender)
    print("Instance: " ,instance)
    print(f'kwargs: {kwargs}')


@receiver(post_save, sender = User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("----------------")
        print("Post Save  signal....")
        print('New Record')
        print("Sender: " , sender)
        print("Created: " ,created)
        print(f'kwargs: {kwargs}')
    else:
        print("----------------")
        print("Post Save  signal....")
        print('Update Record')
        print("Sender: " , sender)
        print("Created: " ,created)
        print(f'kwargs: {kwargs}')


@receiver(pre_delete, sender = User)
def at_beginning_delete(sender,instance,**kwargs):
    print("----------------")
    print("pre Delete  signal....")
    print("Sender: " , sender)
    print('Instance', instance)
    print(f'kwargs: {kwargs}')



@receiver(post_delete, sender = User)
def at_ending_delete(sender,instance,**kwargs):
    print("----------------")
    print("post Delete  signal....")
    print('Instance', instance)
    print("Sender: " , sender)
    print(f'kwargs: {kwargs}')




@receiver(pre_init, sender = User)
def at_beginning_init(sender,*args,**kwargs):
    print("----------------")
    print("Pre init signal....")
    print("Sender: " , sender)
    print('Args', args)
    print(f'kwargs: {kwargs}')


@receiver(post_init, sender = User)
def at_ending_init(sender,*args,**kwargs):
    print("----------------")
    print("post init  signal....")
    print("Sender: " , sender)
    print('Args', args)
    print(f'kwargs: {kwargs}')

    