import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def email_submission(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')

    

    print recipients
    print name
    print message
    # send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)

    send_mail(name, ('From: %s - Email: %s - Message: %s' % (name, email, message)), email, ['sharedslots@gmail.com'], fail_silently=False)

    return HttpResponse('Your Message Has Been Sent, Thank You')