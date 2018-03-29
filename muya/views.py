from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Project
from .forms import FeedbackForm

# Create your views here.
def index(request):
    pro = Project.this_project()

    return render(request, "index.html", {"pro":pro})

def footer(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = FeedbackForm()
    return render(request, "footer.html", {"form":form})
