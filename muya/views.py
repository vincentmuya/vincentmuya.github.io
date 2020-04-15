from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from django.http import JsonResponse
from django.core.mail import mail_admins
from django.http import HttpResponseRedirect
from github import Github

# Create your views here.
from github import Github


# First create a Github instance:
g = Github("5176de4acf199721cbd9d3967372d0da0eb4ea8a")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{vincentmuya}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

def index(request):
    repos = repo.name
    return render(request, "index.html", {"repos":repos})

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
