from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def email(request):
	return render(request,"Client/email.html")

def mail_info(request):
	mailto = request.POST['to']
	mailsubject = request.POST['subject']
	mailmessage = request.POST['msg']

	send_mail(mailsubject, mailmessage, settings.EMAIL_HOST_USER, [mailto], fail_silently=False)
	messages.success(request, 'Email Sent Successfully!')
	return redirect('/Client/email/')
