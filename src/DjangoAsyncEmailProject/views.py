from django.http import HttpResponse
from DjangoAsyncMail.mail import send_html_mail

def mail_send(request):
	result = send_html_mail('Testing','Test HTML Content',['thehobbymania@gmail.com'],['noreply@thehobbymania.com'])
	#result=1
	if result:
		return HttpResponse('Success. Mail Sent.')
	else:
		return HttpResponse('Mail Not Sent.')