from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse
from django.http import JsonResponse
from django.core.mail import mail_admins
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client


# Create your views here.
def index(request):
    return render(request, "index.html")

def skills(request):
    return render(request, "skills.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            sender = form.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(Name, sender)
            Question_or_Feedback = "Question_or_Feedback: {}".format(form.cleaned_data['Question_or_Feedback'])
            mail_admins(subject, Question_or_Feedback)
            contact =form.save(commit=False)
            # contact.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def auto_reply(request):
    # Your Twilio API credentials
    account_sid = 'ACd1e08c8eafd7f15f41ce3d7dd3af0d92'
    auth_token = '55eb13d4eb915a30854c6dfde717dc3f'
    client = Client(account_sid, auth_token)

    # Your Twilio WhatsApp number
    whatsapp_number = 'whatsapp:+14155238886'

    # Retrieve the most recent message in the message log
    message_logs = client.messages.list(from_=whatsapp_number, limit=1)

    if message_logs:
        most_recent_message = message_logs[0]
        if "2" in most_recent_message.body:
            # The user has replied with "2" in the most recent message
            response_body = "Here is the link to our website: https://whatstore.intuinno.com/"
        else:
            # Send the default welcome message
            response_body = 'Welcome to ABC ltd. For Inquiry press 1. To place an order press 2.'
    else:
        # No message logs found, send the default welcome message
        response_body = 'Welcome to ABC ltd. For Inquiry press 1. To place an order press 2.'

    # Send the message
    message = client.messages.create(
        from_=whatsapp_number,
        body=response_body,
        to='whatsapp:+254710902541'
    )

    # Check the message information
    print("Message SID:", message.sid)
    print("Message Status:", message.status)
    print("Message Content:", message.body)

    return JsonResponse({'status': 'Auto-reply sent'})
