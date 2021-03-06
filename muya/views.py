from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.http import JsonResponse
from django.core.mail import mail_admins
from django.http import HttpResponseRedirect

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
