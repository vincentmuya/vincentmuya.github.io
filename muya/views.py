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

def chatbot_response(request):
    user_message = request.GET.get('message', '').lower()

    if "skills" in user_message:
        response = "I specialize in web development, Python, Django, JavaScript, APIs, USSD, Check out more of my skills in the 'Skills' section of my portfolio."
    elif "projects" in user_message:
        response = "I have developed a number of projects from E-commerce to USSD and SMS platforms. Check out my recent projects in the 'Projects' section of my portfolio."
    elif "how long" in user_message or "coding" in user_message or "start" in user_message or "begin" in user_message:
        response = "I've been coding for over 5 years, starting with HTML, CSS and JavaScript and then expanding my expertise over time."
    elif "inspired" in user_message or "inspire" in user_message or "become a developer" in user_message:
        response = "My passion for problem-solving and creating useful applications inspired me to become a developer. There is also the fact I was a taxi driver and when the online taxi services were launched causing a rift from other taxi services. I got intrigued with the technical workings of software and by a couple of months I had enrolled in a coding institution"
    elif "freelance" in user_message:
        response = "Yes, I take on freelance projects when I can! If you'd like or need help with a project, feel free to contact me through the 'Contact' section."
    elif "contract" in user_message:
        response = "Yes, I take on contracts projects when I can! If you'd like or need help with a project, feel free to contact me through the 'Contact' section."
    elif "employment" in user_message:
        response = "I am open to employment! Feel free to contact me through the 'Contact' section."
    elif "employed" in user_message:
        response = "I am open to employment! Feel free to contact me through the 'Contact' section."
    elif "tools" in user_message or "frameworks" in user_message or "framework" in user_message:
        response = "I regularly work with Django, JavaScript, Bootstrap, PostgreSQL, and APIs. Check out more of my skills in the 'Skills' section of my portfolio."
    elif "favorite project" in user_message or "favorite" in user_message:
        response = "One of my favorite projects is Sherehemall. It was exciting because I used most of my for front-end and back-end skills. You can check it out in the 'Projects' section!"
    elif "future goals" in user_message or "developer goals" in user_message or "goals" in user_message or "goal" in user_message:
        response = "I aim to keep improving my skills, work on impactful projects, and learn new technologies like AI and machine learning."
    elif "mentorship" in user_message or "training" in user_message:
        response = "I enjoy helping others learn to code! While I don't currently offer structured mentorship programs, I'm happy to answer questions and provide guidance."
    elif "resume" in user_message or "cv" in user_message or "curriculum vitae" in user_message:
        response = "Sure! You can have my resume. Contact me through the 'Contact' section and I will send it to you."
    elif "hobbies" in user_message or "outside of coding" in user_message:
        response = "I enjoy taking walks, exploring new tech, and contributing to open-source projects."
    else:
        response = "I'm here to help! Ask me about my skills, projects, or anything else."

    return JsonResponse({"response": response})

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
