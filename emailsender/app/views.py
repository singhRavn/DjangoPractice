# from multiprocessing import connection
import json
from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def send_email(request):
    if request.method == "POST":
        with get_connection(host = settings.EMAIL_HOST,port = settings.EMAIL_PORT,username = settings.EMAIL_HOST_USER,password= settings.EMAIL_HOST_PASSWORD,use_tls = settings.EMAIL_USE_TLS) as connection:
            subject = request.POST.get("subject")
            print(request.body)
            email_from = settings.EMAIL_HOST_USER
            # recipient_list = request.POST.get("email").split()  
            data_dict = json.loads(request.body.decode('utf-8'))
            email = data_dict.get("email")
            recipient_list = [email]
            print(recipient_list)
            message = request.POST.get("message")
            EmailMessage(subject,message,email_from,recipient_list,connection=connection).send()
    return render(request,'home.html')