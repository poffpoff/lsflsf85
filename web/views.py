from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail

# Create your views here.

def index(request):
    context = {}
    template = loader.get_template('web/html5up-story/index.html')
    return HttpResponse(template.render(context, request))

def indexdemo(request):

    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("baptiste.declerck@reseau.eseo.fr")
    to_email = Email("baptiste.declerck@reseau.eseo.fr")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

    context = {}
    template = loader.get_template('web/html5up-story/index-demo.html')
    return HttpResponse(template.render(context, request))