from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Project,FeedbackRecipients
from .forms import FeedbackForm
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            question_Feedback = form.cleaned_data['question_Feedback']
            recipient = FeedbackRecipients(email =email,question_Feedback=question_Feedback)
            recipient.save()
            HttpResponseRedirect('/')
    else:
        form = FeedbackForm()
    test = "WORKING"
    pro = Project.this_project()

    return render(request, "index.html", {"pro":pro, 'test':test, 'form':form,})

def skills(request):
    return render(request, "skills.html")
