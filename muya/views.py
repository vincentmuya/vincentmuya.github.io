from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Project,FeedbackRecipients
from .forms import FeedbackForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            question_Feedback = form.cleaned_data['question_Feedback']
            recipient = FeedbackRecipients(email =email,question_Feedback=question_Feedback)
            recipient.save()
            HttpResponseRedirect('index')
    else:
        form = FeedbackForm()
    test = "WORKING"
    pro = Project.this_project()

    return render(request, "index.html", {"pro":pro, 'test':test, 'form':form,})

def footer(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            question_Feedback = form.cleaned_data['question_Feedback']
            recipient = FeedbackRecipients(email =email,question_Feedback=question_Feedback)
            recipient.save()
            HttpResponseRedirect('index')
    else:
        form = FeedbackForm()

    test = "WORKING"
    return render(request, 'footer.html', {'form':form, 'test':test})
