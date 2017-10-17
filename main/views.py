from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from main.forms import EmailForm
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def sendmail(request):
	form = EmailForm(request.POST or None)

	if form.is_valid():
		name = form.cleaned_data.get('name')
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		recipients = [email]

		# send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
		send_mail(name, ('From: %s - Message: %s' % (email, message)), email, ['mukkancom@gmail.com'], fail_silently=False)
		
		return HttpResponse('Your Message Has Been Sent, Thank You')
	context = {
		"form": form,
	}
