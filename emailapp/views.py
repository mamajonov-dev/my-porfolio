from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from Emailsend import settings
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email_ = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'Name: {name}\nPhone: {phone}\nemail: {email_}\nMessage: {message}'
        send_mail('yor email', subject, 'mamajonov.dev@mail.ru', ['mamajonov.dev@gmail.com'], fail_silently=False)


    return render(request, 'index.html')